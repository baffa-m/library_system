from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Categories


class IndexView(TemplateView):
    template_name = "library/index.html"
    
class CategoryCreateView(CreateView):
    model = Categories
    fields = "__all__"
    
    success_url = "/succesful"