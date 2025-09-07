from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("こんにちはya-")

def hobby(request):
    return HttpResponse("My hobby is playing games.")
def greet(request, name):
    message = ("こんにちは",name, "さん")
    return HttpResponse(message)