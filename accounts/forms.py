from django import forms
from .models import *


class ProfileEdit_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'email', 'profile_img', 'id_number']

class UserTypeFilterForm(forms.Form):
    user_type = forms.ChoiceField(
        choices=[
            ('0', 'حساب را انتخاب کنید'),
            ('1', 'کاربر فعال'),
            ('2', 'کاربر مدیر'),
            ('3', 'کاربر دانشجو'),
        ],
        required=False,
    )
