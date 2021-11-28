from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Project, Blog
from django.views.generic import ListView, DetailView

def index(request):
    index_blogs = Blog.objects.all().order_by('-date_posted')[:2]
    content = {
        'index_blogs': index_blogs
    }
    return render(request, 'index.html', content)


def about(request):
    return render(request, 'about.html')

# =============================================

# def project(request):
#     projects = Project.objects.order_by('-date_posted')
#     context = {
#         'projects': projects
#     }
#     return render(request, 'projects.html', context)

# def proj1(request, pk):
#     project = Project.objects.get(pk=pk)
#     context = {
#         'project':project
#     }
#     return render(request, 'proj1.html', context) 


class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']
    paginate_by = 2


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'proj1.html' 
# =============================================

# ======================================================
def blog(request):
    blogs = Blog.objects.order_by('-id')
    single_blogs = Blog.objects.order_by('-date_posted')[:2]
    context = {
        'blogs': blogs,
        'single_blogs': single_blogs,
    }

    return render(request, 'blog.html', context)


def singlepost(request, pk):
    blog = Blog.objects.get(pk=pk)
    alones = Blog.objects.order_by('-date_posted')[:2]
    context = {
        'alones': alones,
        'blog':blog,
    }
    return render(request, 'singlepost.html', context)
# =========================================================

def contact(request):
    return render(request, 'contact.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                return redirect('index')
            
        else:
            messages.info(request, 'Not password matching!')
            return redirect('register')              

    return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')

    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('index')

