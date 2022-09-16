from django.shortcuts import render
from django.views import generic
from .models import Page

import datetime
from django.http import HttpResponse

# Create your views here.
class Page1(generic.ListView):
    # queryset = Page.objects.filter(status=1).order_by('-createdOn')
    template_name = 'page.html'

class Home1(generic.DetailView):
    model = Page
    template_name = 'home2.html'


def Home(request, slug):
    homePage = Page.objects.filter(status=1).order_by('-createdOn')

    context = {
        'home': homePage
    }
    return render(request, "home.html", context)
