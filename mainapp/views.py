from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request, path=None):
    if path is None:
        return render(request, 'mainapp/index.html')

    else:
        return HttpResponseRedirect(reverse("index"))
