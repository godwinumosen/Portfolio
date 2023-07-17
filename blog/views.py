from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth.models import User
from .models import BlogMode

# Create your views here.
def index(request):
    blogs = BlogMode.objects.all()
    context ={
        'blogs':blogs
    }
    return render(request,'index.html',context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Create the user
            new_user = User.objects.create_user(username=username, email=email, password=password)            
            return redirect('/new_user_login') 
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, f'Login successful. Welcome back {username}!')
                return redirect('/index')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'registration/new_user_login.html', {'form': form})


#whatsapp messages
def whatsapp_message(request):
    whatsapp_number = '+2347016087680'
    whatsapp_link = f'https://api.whatsapp.com/send?phone={whatsapp_number}'
    context = {'whatsapp_link': whatsapp_link}
    return render(request, 'whatsapp_message.html', context)
