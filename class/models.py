from django.db import models
from tinymce import models as tinymce_models
from accounts.models import User
from extensions.utils import jalali_converter

# Create your models here.


class ClassCategory(models.Model):
    class Meta:
        verbose_name = "دسته بندی کلاس ها"
        verbose_name_plural = "دسته بندی کلاس ها"

    name = models.CharField(verbose_name="نام دسته", max_length=250)
    
    def __str__(self):
        return self.name
    

class VideoClass(models.Model):
    class Meta:
        verbose_name = "فیلم های کلاس ها"
        verbose_name_plural = "فیلم های کلاس ها"
        
    name = models.CharField(verbose_name="نام فیلم", max_length=250)
    video = models.FileField(verbose_name="فیلم", upload_to="media/")
    
    def __str__(self):
        return self.name
    

class ImageClass(models.Model):
    class Meta:
        verbose_name = "تصاویر کلاس ها"
        verbose_name_plural = "تصاویر کلاس ها"

    name = models.CharField(verbose_name="نام تصویر", max_length=250)
    image = models.FileField(verbose_name="تصویر", upload_to="images/")
    
    def __str__(self):
        return self.name
    
    
class Classes(models.Model):
    class Meta:
        verbose_name = "کلاس ها"
        verbose_name_plural = "کلاس ها"
        
    name = models.CharField(verbose_name="نام کلاس", max_length=250)
    text = tinymce_models.HTMLField(verbose_name="توضیحات کلاس")
    category = models.ForeignKey(ClassCategory, verbose_name="دسته بندی کلاس", on_delete=models.CASCADE)
    img = models.ManyToManyField(ImageClass, verbose_name="تصاویر کلاس", blank=True)
    video = models.ManyToManyField(VideoClass, verbose_name="فیلم های کلاس", blank=True)
    
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    class Meta:
        verbose_name = "دوره ها"
        verbose_name_plural = "دوره ها"

    name = tinymce_models.HTMLField(verbose_name="نام دوره")
    student = models.ForeignKey(User, verbose_name="دانشجو", on_delete=models.CASCADE)
    time_added = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    classes = models.ManyToManyField(Classes, verbose_name="درس های دوره")
    videos = models.ManyToManyField(VideoClass, through='CourseVideo', verbose_name="ویدیوهای دوره", blank=True)

    def __str__(self):
        return self.name

    def jtime_added(self):
        return jalali_converter(self.time_added)

class CourseVideo(models.Model):
    class Meta:
        verbose_name = "ویدیوهای دوره"
        verbose_name_plural = "ویدیوهای دوره"

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.ForeignKey(VideoClass, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.name} - {self.video.name}"