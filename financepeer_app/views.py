from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .form import JSONForm, handleFileUpload
from .models import Blog
# Create your views here.

def signup(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            username = user_creation_form.cleaned_data.get('username')
            raw_password = user_creation_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('task:home')
    else:
        user_creation_form = UserCreationForm()
    return render(
        request,
        template_name="registration/signup.html",
        context={"user_creation_form": user_creation_form},
    )


@login_required(login_url="/accounts/login/")
def home(request):
    blogs = Blog.objects.all().order_by('-created_date')
    if request.method == 'POST':
        form = JSONForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            handleFileUpload( uploaded_file.read())
            return redirect('task:home')
    else:
        form = JSONForm()
    return render(request, template_name="home.html", context={'form' : form, 'blogs':blogs})
