from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from myApp.models import *
from myApp.forms import PostForm, CommentForm
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        "posts":posts,
    }
    return render(request,"index.html",context)

def detail(request, id):
    post_detail = get_object_or_404(Post, id=id)

    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post_detail
        comment.save()
        return HttpResponseRedirect("/"+str(id)+'/detail/')
        
    context = {
        'post_detail': post_detail,
        'forms': form,
    }
    return render(request,'detail.html',context)

def postCreate(request):
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = PostForm()
    else:
        form = PostForm()
    
    context = {
        'form':form
    }
    return render(request,'forms.html',context)

def postUpgrade(request,id):
    post_upgrade = get_object_or_404(Post, id=id)
    print('post update', post_upgrade)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post_upgrade)
        print('form', form)
        if form.is_valid():
            form.save()
            form = PostForm()
            return redirect('index')
    else:
        form = PostForm()
        
    context = {
        'form': form
    }
    return render(request, 'forms.html', context)
    
    
    

def postDelete(request,id):
    post_delete = get_object_or_404(Post, id=id)
    post_delete.delete()
    
    return HttpResponseRedirect('/')


