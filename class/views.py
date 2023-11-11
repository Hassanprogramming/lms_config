from django.shortcuts import render
from django.views import View
from .models import Classes

# Create your views here.

class ClassesView(View):
    def get(self, request):
        courses = Classes.objects.all()
        context = {
            "courses": courses,
        }
        return render(request, "class/classes.html", context)