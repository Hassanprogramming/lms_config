from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Classes

class ClassesView(View):
    def get(self, request):
        courses = Classes.objects.filter(display=True)

        if request.user.is_authenticated:
            selected_courses = Classes.objects.filter(user=request.user, display=True)
        else:
            selected_courses = None

        context = {
            "courses": courses,
            "selected_courses": selected_courses,
        }
        return render(request, "class/classes.html", context)

class CourseDetailView(View):
    def get(self, request, slug):
        course = get_object_or_404(Classes, slug=slug)
        print(course.video.all())
        context = {
            "course": course,
        }
        return render(request, "class/course_detail.html", context)
