from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    #if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        #if the form is valid
        if form.is_valid():
            #yes, save
            form.save()

            #redirect to home 
            return HttpResponseRedirect('/')

            #no, show error
        else:
            return HttpResponseRedirect(form.errors.as_json())




    #get all posts limit 20
    posts = Post.objects.all().order_by("-created_at")[:20]
    form = PostForm
    #Show
    return render(request, 'posts.html', {'posts': posts})


def delete(request, post_id):
    # find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def LikeView(request,post_id):
    post = Post.objects.get(id= post_id)

    new_value = post.likes + 1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')

def edit(request,post_id):
    if request.method == "GET":
        posts = Post.objects.get(id=post_id)
        return render(request,'edit.html',{'posts':posts})
    if request.method == 'POST':
        editposts = Post.objects.get(id=id)
        form= PostForm(request.POST, request.FILES, instance=editposts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("not valid")
        