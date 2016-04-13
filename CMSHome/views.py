from django.shortcuts import render


def home(request):
    context = {'Title':"Home - ChMS", }
    return render(request, 'index.html', context)