from django.db import models
from tinymce import models as tinymce_models
from accounts.models import User
from extensions.utils import jalali_converter
from django.template.defaultfilters import slugify

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
    text = tinymce_models.HTMLField(verbose_name="توضیحات فیلم")
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
        
    user = models.ForeignKey(User, verbose_name="دانشجو", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="نام کلاس", max_length=250)
    text = tinymce_models.HTMLField(verbose_name="توضیحات کلاس")
    category = models.ForeignKey(ClassCategory, verbose_name="دسته بندی کلاس", on_delete=models.CASCADE)
    display = models.BooleanField(verbose_name="نمایش داده شود؟؟", default=False)
    total_hours = models.FloatField(verbose_name="مدت زمان کل دوره", null=True, blank=True)
    img = models.ManyToManyField(ImageClass, verbose_name="تصاویر کلاس", blank=True)
    video = models.ManyToManyField(VideoClass, verbose_name="فیلم های کلاس", blank=True)
    slug = models.SlugField(max_length=150, unique=True)

    def save(self, *args, **kwargs):
        # Generate slug when saving the model
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
