from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    bprofile = BlogProfile.objects.get(pk=1)
    carousel = Blog_Post.objects.filter(featured=True)
    newpost = Blog_Post.objects.all().order_by('-created_on')
    p = Paginator(newpost,10)
    page = request.GET.get('page')
    pagine = p.get_page(page)
    

    context = {
        'bprofile' : bprofile,
        'pagine' : pagine,
        'carousel':carousel,
    }

    return render(request, 'index.html', context)

def detail(request, theslug):
    trendsongs = Blog_Post.objects.filter(trendsongs=True)
    mostviewed = Blog_Post.objects.filter(mostviewed=True)
    detail = Blog_Post.objects.get(slug=theslug)
    comments = Comment.objects.order_by('-id').filter(post=detail)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            thecom = form.save(commit=False)
            thecom.post = detail
            thecom.commenter = request.user
            thecom.save()
            return redirect('detail', theslug=detail.slug)

    context = {
        'trendsongs':trendsongs,
        'mostviewed':mostviewed,
        'detail':detail,
        'comments':comments,
        'form':form
    }

    return render(request, 'detail.html', context)


def post_like(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Blog_Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'like':
                like.value = 'unlike'
            else:
                like.value = 'like'

        like.save()
    return redirect('home')

def category(request, id, slug):
    newcat = Category.objects.get(slug=slug)
    news = Blog_Post.objects.filter(category_id=id)

    context = {
        'news':news,
        'newcat':newcat,
    }

    return render(request, 'category.html', context) 

def signout(request):
    logout(request)
    messages.success(request, 'You have successfully signed out!')
    return redirect('home')
  

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'login successful!')
            return redirect('home')
        else:
            messages.info(request, 'Username/Password is incorrect, please try again.')
            return redirect('signin')

    return render(request, 'signin.html')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            newuser = Visitor(user=user)
            newuser.first_name = user.first_name
            newuser.last_name = user.last_name
            newuser.email = user.email
            newuser.save()
            messages.success(request, 'signup succesful')
            return redirect ('home')
        else:
            messages.error(request, form.errors)

    return render(request, 'signup.html')

def search(request):
    if request.method == 'POST':
        items = request.POST['search']
        searched = Q(Q(title__icontains=items))
        searched_item = Blog_Post.objects.filter(searched)
        context = {
            'items':items,
            'searched_item':searched_item
        }

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')