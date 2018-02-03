from django.shortcuts import render
from django.http import JsonResponse

from . import classify


def index(request):
    return render(request, 'classifier_app/index.html')


def ajax_classify(request, handle):
    return JsonResponse({'coefficients': classify.classify(handle)})


def ajax_classify_tweet(request):
    if request.method == 'POST':
        tweet = request.POST['tweet'][0]
        return JsonResponse({'coefficients': classify.classify_tweet(tweet)})
    else:
        return JsonResponse({'coefficients': [0.0, 0.0, 0.0, 0.0]})
