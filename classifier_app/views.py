from django.shortcuts import render
from django.http import JsonResponse

from . import classify


def index(request):
    return render(request, 'classifier_app/index.html')


def ajax_classify(request, handle):
    return JsonResponse({'coefficients': classify.classify(handle)})
