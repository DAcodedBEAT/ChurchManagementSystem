from django.shortcuts import HttpResponse, render


def dashboard(request):
    return HttpResponse("Dashboard")


def input_income(request):
    return HttpResponse("input income")


def edit_income(request):
    return HttpResponse("edit income")


def edit_specific_income(request):
    return HttpResponse("edit specific income")


def delete_income(request):
    return HttpResponse("delete income")


def delete_specific_income(request):
    return HttpResponse("delete specific income")


def upload_income(request):
    return HttpResponse("upload income")


def download_income(request):
    return HttpResponse("download income")


def download_sheet_income(request):
    return HttpResponse("download sheet income")


def download_all_incomes(request):
    return HttpResponse("download all incomes")


def view_pledge(request):
    return HttpResponse("view pledge")


def my_pledge(request):
    return HttpResponse("my pledge")