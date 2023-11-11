from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group
from extensions.utils import jalali_converter

class UserManager(BaseUserManager):
    def create_user(self, name, password, phone, email, **other_fields):
        if not name:
            raise ValueError("نام کاربری یک فیلد اجباری است.")
        if not password:
            raise ValueError("رمز عبور یک فیلد اجباری است")
        if not phone:
            raise ValueError("شماره تلفن یک فیلد اجباری است")
        if not email:
            raise ValueError("ایمیل یک فیلد اجباری است")
        
        user = self.model(name=name, phone=phone, email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None, **other_fields):
        user = self.create_user(password=password, **other_fields)
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.is_student = True
        user.confirm_profile = True
        user.save(using=self._db)
        return user 


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        
    name = models.CharField(verbose_name="نام کاربری", unique=True, max_length=20)
    phone = models.BigIntegerField(verbose_name="شماره تلفن", unique=True)
    email = models.EmailField(verbose_name="ایمیل", max_length=100)
    id_number = models.FloatField(verbose_name="کد ملی", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    is_admin = models.BooleanField(default=True, verbose_name="مدیر")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_student = models.BooleanField(default=True, verbose_name="دانشجو")
    profile_img = models.ImageField(upload_to='images/', verbose_name="تصویر پروفایل")
    password1 = models.CharField(max_length=150, verbose_name="رمز عبور")
    password2 = models.CharField(max_length=150, verbose_name="تایید رمز عبور")
    objects = UserManager()
    USERNAME_FIELD = 'name'
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="user_permissions", verbose_name="دسترسی‌ها")
    groups = models.ManyToManyField(Group, blank=True, related_name="groups", verbose_name="گروه‌ها")
    REQUIRED_FIELDS = ['phone', 'email']

    def save(self, *args, **kwargs):
        if not self.pk and self.password1 and self.password2:
            # Perform password validation and hashing when creating a new user
            if self.password1 != self.password2:
                raise ValueError("Passwords do not match.")
            self.set_password(self.password1)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def jlast_login(self):
        return jalali_converter(self.last_login)

    def jtime(self):
        return jalali_converter(self.date_created)

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def imageURL(self):
        try:
            url = self.profile_img.url
        except:
            url = ''
        return url
