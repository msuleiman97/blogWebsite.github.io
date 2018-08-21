from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm,EditProfileForm
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            #login the user
            login(request, user)
            return redirect('articles:list')
        # Redirect to a success page.
        
        else:
            form=RegistrationForm()
            return render(request, 'accounts/signup.html', { 'form': form })
        # Return an 'invalid login' error message.
        ...
        """if form.is_valid():
            
            user=form.save()

            
            #login the user
            login(request,user)
            return redirect('articles:list')"""
    else:
        
        form=RegistrationForm()
    return render(request,'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            #login  the user
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form=AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})



def logout_view(request):
    if request.method == 'POST':
        
        
        logout(request)
        return redirect('articles:list')
        #return HttpResponse('you are logged out')
        
@login_required(login_url='/accounts/login/')     
def profile(request):
    profile=request.user.UserProfile
    args={'user':request.user ,'profile':profile}
    return render(request,'accounts/profile.html',args)
def friends(request):
    return render(request,'accounts/friends.html')

def edit_profile(request):
    if request.method == 'POST':
        form=EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/accounts/profile")
    else:
        form =EditProfileForm(instance=request.user)
        args= {'form':form}
        return render(request,'accounts/edit_profile.html', args)
           
def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
    else:
        form =PasswordChangeForm(user=request.user)
        args= {'form':form}
        return render(request,'accounts/change_passwoord.html', args)
             