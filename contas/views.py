from django.shortcuts import render
from django.views import generic


class HomepageView(generic.TemplateView):
    template_name = "homepage.html"
