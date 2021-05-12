from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'average': 200, 'max': 300, 'min': 100, 'recommended': 220})


def about(request):
    return render(request, 'main/about.html')