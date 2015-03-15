from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render, redirect, get_list_or_404

from Accounts.models import User, UserProfile
from Accounts.forms import UserRegisterForm, UserCreationForm


def user_register(request):
    """
    Creates page to register a new user.
    """
    if request.user.is_anonymous():  # If there is no logged in user
        context = {}     # Add CSRF token
        context.update(csrf(request))
        if request.method == 'POST':
            # Build the form, and validate it
            user_form = UserRegisterForm(request.POST)
            if user_form.is_valid():
                if User.objects.filter(username__iexact=user_form.username) != 0:
                    user_form.save()
                    messages.success(request, "User Account Created. Please fill out profile details.")
                    return redirect('accounts.views.create_profile')
                else:
                    messages.error(request, "This Username has already been taken.  Please find another one.")
                    context['user_form'] = user_form
                    return render(request, 'register.html', context)
            else:
                messages.error(request, "An Error has occurred.")
                context['user_form'] = user_form
                return render(request, 'register.html', context)
        else:
            user_form = UserRegisterForm()
        context['user_form'] = user_form
        return render(request, 'register.html', context)
    else:
        return redirect('views.dashboard')


def user_login(request):
    """
    Creates page to log a user in.
    """
    if request.user.is_anonymous():
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active():
                    login(request, user)
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                else:
                    messages.error(request, "Not an active account.")
                    return render(request, 'login.html')
            else:
                messages.error(request, "Wrong username/password.")
                return render(request, 'login.html')
        else:
            context = {}
            context.update(csrf(request))
            return render(request, 'login.html', context)
    return redirect('views.dashboard')


def user_logout(request):
    """
    Logs out the currently logged in user.
    """
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('views.dashboard')


def view_user(request, user_id=None):
    """
    View the User's page
    """

    if user_id is not None:
        user_list = get_list_or_404(User, username__iexact=user_id)
        if user_list.count() == 1:
            user = user_list[:1].get()
            if user.username == user_id:
                context = [user]
                return render(request, 'accounts/view_user.html', context)
            else:    # user has a different capitalization
                return redirect('Accounts.view_user', user_id=user.username)
        else:
            messages.error(request, "User Request is not Valid.")
            raise Http404