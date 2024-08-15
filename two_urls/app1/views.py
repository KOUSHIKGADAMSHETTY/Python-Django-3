from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def one(request,p,t,r):
    si = (p*t*r)/100
    greetings = (f"your SI {si}")
    return HttpResponse(greetings)
