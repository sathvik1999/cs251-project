from django.utils import timezone
from .models import Interest,Document,Rate,Follow,Community,Join,JoinPending
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm,InterestForm,DocumentForm,RatingForm,CommunityForm
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .filters import DocumentFilter

@login_required
def home(request):
    documents = Document.objects.order_by('published_date').filter(uploader=request.user.username.encode('ascii','ignore'))
    interest = Interest.objects.filter(user=request.user).order_by('-published_date').first()
    doc=Document.objects.order_by('published_date').filter(genre__in=interest.my_field)
    f=Follow.objects.get(user=request.user)
    fl=f.flist.all()
    Communities=Community.objects.all().exclude(admin=request.user)
    communities=[c for c in Communities]
    jpclist=map(lambda x:[x,JoinPending.objects.get(com=x).jplist.all()],communities)
    oCom=Community.objects.filter(admin=request.user)
    ocom=[c for c in oCom]
    opclist=map(lambda x:[x,JoinPending.objects.get(com=x).jplist.all().count()],ocom)
    jcom=Join.objects.get(user=request.user).jlist.all()
    #if Community.objects.filter(admin=request.user):
     #   jreq=Community.objects.get(admin=request.user).jrequests.all()
    #else:
     #   jreq=[]
    return render(request, 'home.html',{'documents': documents,'interest':interest,'doc':doc,'fl':fl,'jpclist':jpclist,'jcom':jcom,'opclist':opclist})

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
            Follow.objects.create(user=user)
            Join.objects.create(user=user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

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
            post.user=request.user
            post.uploader = request.user.username.encode('ascii','ignore')
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {'form': form})

def search(request):
    Document_list = Document.objects.all()
    Document_filter = DocumentFilter(request.POST, queryset=Document_list)    
    if request.method == 'POST':
        le=Document_list.count()
        return render(request, 'search.html', {'filter': Document_filter,'le':le})
    else:
        return render(request, 'search.html',{'filter': Document_filter,'le':0})

def delete1(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    doc.delete()
    return redirect('home')

def bookpage(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            r = Rate.objects.filter(doc=doc,user=request.user)
            if not r:
                r=Rate.objects.create(user=request.user, doc=doc, rating=form.cleaned_data.get('rating',None))
            r=Rate.objects.get(doc=doc,user=request.user)
            r.rating=form.cleaned_data.get('rating',None)
            r.save()
            tr=list(Rate.objects.filter(doc=doc).values_list('rating',flat=True))
            #print(r.rating)
            #print(Rate.objects.get(doc=doc,user=request.user).rating)
            if tr!=[]:
                r1=float(sum(tr))/float(len(tr))
                print(tr)
                t=len(tr)
                d1=Document.objects.get(document=doc.document)
                d1.rate1=r1
                d1.no_ratings=t
                d1.save()
            else:
                r1=0
                t=0
                doc.rate1=r1
                doc.no_ratings=t
                doc.save()
            return render(request,'bookpage.html',{'doc':doc,'form':form,'r':r,'r1':round(r1,2),'t':t,'user':request.user})
    else:
        form = RatingForm()
        tr=list(Rate.objects.filter(doc=doc).values_list('rating',flat=True))
        if tr!=[]:
            r1=float(sum(tr))/float(len(tr))
            t=len(tr)
            doc.rate=r1
            doc.no_ratings=t
            doc.save()
        else:
            r1=0
            t=0
            doc.rate=r1
            doc.no_ratings=t 
            doc.save() 
    return render(request,'bookpage.html',{'doc':doc,'form':form,'r1':round(r1,2),'t':t})

def reset(request):
    return redirect('home')

def genre(request,pk):
    documents=Document.objects.filter(genre=pk)
    return render(request,'genre.html',{'docs':documents})

def author(request,pk):
    documents=Document.objects.filter(author=pk)
    return render(request,'author.html',{'docs':documents})

def uploader(request,pk):
    documents=Document.objects.filter(uploader=pk)
    u=documents.first().user
    f=Follow.objects.get(user=request.user).flist.all()
    if u in f:
        s=1
    else:
        s=0
    return render(request,'uploader.html',{'docs':documents,'s':s})


def follow(request,pk):
    documents=Document.objects.filter(uploader=pk)
    u=documents.first().user
    f=Follow.objects.get(user=request.user)
    f.flist.add(u)
    f.save()
    return render(request,'uploader.html',{'docs':documents,'s':1})


def unfollow(request,pk):
    documents=Document.objects.filter(uploader=pk)
    u=documents.first().user
    f=Follow.objects.get(user=request.user)
    f.flist.remove(u)
    f.save()
    return render(request,'uploader.html',{'docs':documents,'s':0})


def change(request,pk):
    doc = get_object_or_404(Document, pk=pk)
    doc.public=not(doc.public)
    doc.save()
    form = RatingForm()
    tr=list(Rate.objects.filter(doc=doc).values_list('rating',flat=True))
    if tr!=[]:
        r1=float(sum(tr))/float(len(tr))
        t=len(tr)
        doc.rate=r1
        doc.no_ratings=t
        doc.save()
    else:
        r1=0
        t=0
        doc.rate=r1
        doc.no_ratings=t 
        doc.save() 
    return render(request,'bookpage.html',{'doc':doc,'form':form,'r1':round(r1,2),'t':t})

def community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.admin=request.user
            post.save()
            JoinPending.objects.create(com=post)
            return redirect('home')
    else:
        form = CommunityForm()
    return render(request, 'createcommunity.html', {'form': form})
    
def cpage(request, pk):
    com = get_object_or_404(Community, pk=pk)
    mlist=com.members.all()
    jplist=JoinPending.objects.get(com=com).jplist.all()
    return render(request,'cpage.html',{'com':com,'mlist':mlist,'jplist':jplist})

def srequest(request, pk):
    com = get_object_or_404(Community, pk=pk)
    com.jrequests.add(request.user)
    JoinPending.objects.get(com=com).jplist.add(request.user)
    return redirect('home')

def crequest(request, pk):
    com = get_object_or_404(Community, pk=pk)
    com.jrequests.remove(request.user)
    JoinPending.objects.get(com=com).jplist.remove(request.user)
    return redirect('home')

def accept(request, pk):
    u = User.objects.get(pk=pk)
    com=get_object_or_404(Community, admin=request.user)
    com.members.add(u)
    com.jrequests.remove(u)
    Join.objects.get(user=u).jlist.add(com)
    JoinPending.objects.get(com=com).jplist.remove(u)
    return redirect('cpage',pk=com.pk)

def leave(request, pk):
    com = get_object_or_404(Community, pk=pk)
    com.members.remove(request.user)
    Join.objects.get(user=request.user).jlist.remove(com)
    return redirect('home')