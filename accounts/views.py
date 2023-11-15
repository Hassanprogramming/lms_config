from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class AccountView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_admin:
            form = UserTypeFilterForm(request.GET)
    
            if form.is_valid():
                selected_user_type = form.cleaned_data['user_type']
    
                if selected_user_type == '2':
                    users = User.objects.filter(is_admin=True)
                elif selected_user_type == '3':
                    users = User.objects.filter(is_student=True)
                elif selected_user_type == '1':
                    users = User.objects.filter(is_active=True)
                else:
                    users = User.objects.all()  # Show all users when no user type is selected
            else:
                users = User.objects.all()  # Show all users by default
    
            return render(request, 'accounts/accounts.html', {'users': users, 'form': form})
        else:
            return redirect('access')

class UserAccountView(View):
    @method_decorator(login_required)
    def get(self, request, pid):
        if request.user.is_admin:
            users = get_object_or_404(User, pk=pid)
            form = ProfileEdit_Form(instance=users)
            context = {
                'form': form,
                'users': users,
            }
            return render(request, 'accounts/profile_details.html', context)
        else:
            return redirect('access')
    
    @method_decorator(login_required)
    def post(self, request, pid):
        if request.user.is_admin:
            users = get_object_or_404(User, pk=pid)
            form = ProfileEdit_Form(request.POST, request.FILES, instance=users)
            if form.is_valid():
                form.save()
                return redirect('accounts')
            else:
                context = {
                    'form': form,
                    'users':users
                }
            return render(request, 'accounts/profile_details.html', context)
        else:
            return redirect('access')



        
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        context={
            'form': form, 
        }
        return render(request, 'accounts/login.html', context)
    
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    
class ProfileEditView(View):
    @method_decorator(login_required)
    def get(self,request):
        form = ProfileEdit_Form(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/profile.html', context)
    
    @method_decorator(login_required)
    def post(self,request):
        form = ProfileEdit_Form(request.POST, request.FILES, instance=request.user)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form
            }
            return render(request, 'accounts/profile.html', context)
        
        
@method_decorator(login_required, name='dispatch')
class DeleteAccountView(LoginRequiredMixin, View):
    def get(self, request):
        # Delete the user account and log them out
        user = request.user
        user.delete()
        return redirect('home')