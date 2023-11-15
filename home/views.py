from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "home/home.html")
    
    
class AboutView(View):
    def get(self, request):
        about_content = AboutUs.objects.first()
        context = {
            "about_content": about_content,
        }
        return render(request, "home/about.html", context)
    
    
class ContactView(View):
    def get(self, request):
        return render(request, "home/contact_us.html")