from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *
from home.forms import AddCommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


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
        video_category = VideoCategory.objects.filter(videoclass__in=course.video.all()).distinct()
        form = AddCommentForm()
        context = {
            "course": course,
            "video_category": video_category,
            "form": form,
        }
        return render(request, "class/course_detail.html", context)

    def post(self, request, slug):
        course = get_object_or_404(Classes, slug=slug)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = course
            comment.save()
            messages.success(request, "Comment added successfully.")
            return HttpResponseRedirect(reverse("course_detail", args=[slug]))
        else:
            # If the form is not valid, display error messages using Django messages framework
            for errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            context = {"course": course, "form": form}
            return render(request, self.template_name, context)