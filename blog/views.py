from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import UserModelForm



# Create your views here.


def index(request):
    return render(request,'index.html',{})

def signup(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            # Process the form data
            field_value = form.cleaned_data['field_name']
            # ...
    else:
        form = UserModelForm()
        
    context = {
        'form':form
    }

    return render(request, 'registration/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

#whatsapp messages
def whatsapp_message(request):
    whatsapp_number = '+2347016087680'
    whatsapp_link = f'https://api.whatsapp.com/send?phone={whatsapp_number}'
    context = {'whatsapp_link': whatsapp_link}
    return render(request, 'whatsapp_message.html', context)
