from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignupForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from. models import Post
from django.contrib.auth.models import Group


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user_post = request.user)
        # posts = Post.objects.all()
        full_name = request.user.get_full_name()
        print(full_name)
        return render(request, "blog/dashboard.html", {'posts': posts, 'full_name': full_name})
    else:
        return HttpResponseRedirect('/login/')


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,"Welcome, Account is created")
            user = form.save()
            # group = Group.objects.get(name='Author')
            # user.groups.add(group)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, "blog/signup.html", {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request, data= request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully !!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, "blog/login.html", {'form': form})
    else:
        return  HttpResponseRedirect('/dashboard/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form= PostForm(request.POST)
            if form.is_valid():
                # post = form.save(commit=False)
                # post.user_post = request.user
                form.save() 
                form = PostForm()
                # form.save()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
        

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi= Post.objects.get(pk=id)
            form = PostForm(reaquest.POST, instance=pi)
            if form.is_valid:
                form.save()
        else:
            pi= Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    

def delete_post(request, id):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')