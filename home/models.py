from django.db import models

class AboutUs(models.Model):
    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"
        
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"
        
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    
class Comment(models.Model):
    class Meta:
        verbose_name = "کامنت ها"
        verbose_name_plural = "کامنت ها"
        
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.email} - {self.timestamp}"