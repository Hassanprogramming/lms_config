from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class HomeView(View):
    def get(self, request):
        form = AddCommentForm()
        context = {
            "form": form
        }
        return render(request, "home/home.html", context)
    
    def post(self, request):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            # If the form is not valid, display error messages using Django messages framework
            for errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            context = {"form": form}
            return render(request, "home/home.html", context)
    
    
class AboutView(View):
    def get(self, request):
        about_content = AboutUs.objects.first()
        context = {
            "about_content": about_content,
        }
        return render(request, "home/about.html", context)
    
    
class ContactView(View):
    def get(self, request):
        form = AddcontactForm()
        context = {
            "form": form
        }
        return render(request, "home/contact_us.html", context)
    
    def post(self, request):
        form = AddcontactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            # If the form is not valid, display error messages using Django messages framework
            for errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            context = {"form": form}
            return render(request, "home/home.html", context)