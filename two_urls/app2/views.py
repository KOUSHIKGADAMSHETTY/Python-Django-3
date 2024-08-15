from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
    greetings = "Good Morning!"
    return HttpResponse(greetings)
def two(request):
    greetings = "Have a nice day!"
    return HttpResponse(greetings)