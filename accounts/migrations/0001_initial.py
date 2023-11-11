# Generated by Django 4.2.7 on 2023-11-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('phone', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_student', models.BooleanField(default=True)),
                ('profile_img', models.ImageField(upload_to='images/')),
                ('password1', models.CharField(max_length=150)),
                ('password2', models.CharField(max_length=150)),
                ('groups', models.ManyToManyField(blank=True, related_name='groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'کاربران',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]