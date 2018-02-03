from django.shortcuts import render


def index(request):
    return render(request, 'classifier_app/index.html')
