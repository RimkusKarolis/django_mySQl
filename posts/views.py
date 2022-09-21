from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm
from django.contrib import messages

# displaying all posts
def list_posts(request):
    posts = Post.objects.all()
    return render(request, "main.html", {"posts": posts})


#creating a new post
def create_post(request):
    new_fullName = request.POST["fullName"]
    new_date = request.POST["date"]
    new_fullUrl = request.POST["fullUrl"]
    new_comment = request.POST['comment']

    if new_fullName == "" or new_date == "" or new_fullUrl =="" or new_comment == "":
        posts = Post.objects.all()
        return render(
            request, "main.html", {"post": posts, "error": "fields are required"}
        )
    post = Post(fullName=new_fullName, date=new_date, fullUrl=new_fullUrl, comment=new_comment)
    post.save()

    return redirect("/posts/")
##messages.success(request, "Message sent." )

# function delete post
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("/posts/")

#function which calls another route takes, data from database and displaying into form fields
def edit_post(request, id):  
    posts = Post.objects.get(id=id)  
    return render(request,'edit.html', {'posts':posts}) 

#function updating fields, after update returning to main page.
def update_post(request, id):  
    post = Post.objects.get(id=id)  
    form = PostForm (request.POST, instance = post)  
    if form.is_valid():  
        messages.success(request, "Message sent." )
        form.save()
        messages.success(request, "Message sent." )
        return redirect("/posts")
    messages.success(request, "Message sent." )    
    return render(request, 'edit.html', {'post': post})  

