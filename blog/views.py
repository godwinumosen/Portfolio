from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib import messages
from .forms import RegistrationForm
from .forms import LoginForm,AddPostForm
from .forms import AddPostForm
from django.contrib.auth.models import User
from .models import BlogMode

# Create your views here.

def base (request):
    return render(request,'base.html',{})

def index(request):
    blogs = BlogMode.objects.all()
    context ={
        'blogs':blogs
    }
    return render(request,'index.html',context)

#detail page
def detail_view(request, pk):
    object = get_object_or_404(BlogMode, pk=pk)
    return render(request, 'detail.html', {'detail': object})

#about
def about_author (request):
    about_author = BlogMode.objects.all()
    contex={
        'about_author':about_author
    }
    return render(request,'about_author.html',contex)

#contact
def author_info (request):
    email='umosengodwin568@gmail.com'
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        messages.success(request, f'Your email was sent Successfully we will get back to you {message_name}..!')
        return redirect('/index')
    else:
        context={
            'email':email
        }
        return render(request,'author_info.html',context)

#register user
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

#login user
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


#create blog or add post
def add_post(request):
    if request.method == 'POST':
        form =AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index') 
    else:
        form = AddPostForm()
    return render(request, 'add_post.html', {'form': form})

#edit blog or add post
def update_post(request, pk):
    object = get_object_or_404(BlogMode, pk=pk)
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=pk)
    else:
        form = AddPostForm()
    return render(request, 'update_post.html', {'form': form},{'detail': object})

