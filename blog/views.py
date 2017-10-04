from django.utils import timezone
from .models import Interest,Document
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate
from .forms import SignUpForm,InterestForm,DocumentForm
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .filters import DocumentFilter

@login_required
def home(request):
    documents = Document.objects.order_by('published_date').filter(user=request.user)
    interest = Interest.objects.filter(user=request.user).order_by('-published_date').first()
    doc=Document.objects.order_by('published_date').filter(genre__in=interest.my_field)
    return render(request, 'home.html',{'documents': documents,'interest':interest,'doc':doc})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            Interest.objects.create(user=user,my_field=['fiction'])
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def upload(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
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
            #post.genre= form.cleaned_data['Interests']
            post.published_date =timezone.now()
            post.save()
            return redirect('home')
    else:
        form = InterestForm()
    return render(request, 'interests.html', {'form': form})

def upfile(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {'form': form})

def search(request):
    Document_list = Document.objects.all()
    Document_filter = DocumentFilter(request.GET, queryset=Document_list)
    le=Document_list.count()
    return render(request, 'search.html', {'filter': Document_filter,'le':le})

def delete1(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    doc.delete()
    return redirect('home')
