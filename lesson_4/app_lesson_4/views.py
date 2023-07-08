from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return HttpResponse('homework for 4 assignments')
