from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test1(reqest):
    return HttpResponse('this is awesome')


def about(reqest):
    return HttpResponse('this is about')
