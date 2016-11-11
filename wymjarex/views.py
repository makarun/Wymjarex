from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
#import matplotlib.pyplot as plt

# Create your views here.
@login_required
def posts_list(request):
    posts = Post.objects.filter(author= request.user,created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'wymjarex/posts_list.html', {'posts' : posts})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.created_date = timezone.now()
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm(initial={"created_date": "YYYY-MM-DD"})
    return render(request, 'wymjarex/post_new.html', {'form': form})

@login_required
def last(request, pk):    
    start_date = datetime.now()-timedelta(days = int(pk))
    end_date = datetime.now()
    posts = Post.objects.filter(author= request.user, created_date__gte=start_date, created_date__lte=end_date).order_by('-created_date')
    return render(request, 'wymjarex/posts_list.html', {'posts' : posts})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post.objects.filter(author= request.user), pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'wymjarex/post_edit.html', {'form': form})
