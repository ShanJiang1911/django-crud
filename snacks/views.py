from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView

class HomePageView(TemplateView):
    template_name = "home.html"

