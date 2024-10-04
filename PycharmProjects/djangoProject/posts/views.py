from django.shortcuts import render
from django.http import HttpResponse
import random


def test_view(request):
    return HttpResponse('Hello World!')

def main_page_view(request):
    return render(request, 'base.html')

