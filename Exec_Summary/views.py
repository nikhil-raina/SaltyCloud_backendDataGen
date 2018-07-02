from django.shortcuts import render


def home(request):
    return render(request, 'exec_Summary.html')
