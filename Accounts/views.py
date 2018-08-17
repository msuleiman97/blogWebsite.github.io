from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        
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
            form=UserCreationForm()
            return HttpResponse('worng data entered!')
        # Return an 'invalid login' error message.
        ...
        """if form.is_valid():
            
            user=form.save()

            
            #login the user
            login(request,user)
            return redirect('articles:list')"""
    else:
        
        form=UserCreationForm()
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