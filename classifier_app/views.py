from django.shortcuts import render
from django.http import JsonResponse

from . import classify


def index(request):
    return render(request, 'classifier_app/index.html')


def ajax_classify(request, handle):
    try:
        return JsonResponse({'coefficients': classify.classify(handle)})
    except:
        return JsonResponse({})


def ajax_classify_tweet(request):
    try:
        tweet = request.POST['tweet']
        return JsonResponse({'coefficients': classify.classify_tweet(tweet)})
    except:
        return JsonResponse({})
