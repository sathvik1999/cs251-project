from django.utils import timezone
from .models import Post,Interest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate
from .forms import SignUpForm,PostForm,InterestForm
from django.shortcuts import redirect, render, get_object_or_404


@login_required
def home(request):
    posts = Post.objects.order_by('published_date')
    posts1 = Interest.objects.filter(user=request.user).order_by('-published_date')
    return render(request, 'home.html',{'posts': posts,'posts1':posts1})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def upload(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.uploader = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'upload.html', {'form': form})

def interests(request):
    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.genre= form.cleaned_data['Interests']
            post.published_date =timezone.now()
            post.save()
            return redirect('home')
    else:
        form = InterestForm()
    return render(request, 'interests.html', {'form': form})

