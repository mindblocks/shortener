
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from backend.models import Shortener

# Create your views here.

def redirector(request, slug):

    try:
        url = Shortener.objects.get(slug=slug).url
    except:
        return render(request, 'frontend/404.html')
    return redirect(url)
