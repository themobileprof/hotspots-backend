from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def collect(request):
    return HttpResponse("Tweet collector.")


def process(request):
    return HttpResponse("Tweets processor.")