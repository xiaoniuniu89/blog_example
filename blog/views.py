from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Blog

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'blog/blog_list.html', {'blogs': blogs})





@login_required
def create_blog(request):
    
    if request.method=='POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user = request.user
        Blog.objects.create(
            title = title,
            body = body,
            author = user
        )
        
        return redirect('blog_list')
        
    return render(request, 'blog/blog_create.html', {})


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

@login_required
def blog_edit(request, pk):
    blog = Blog.objects.get(pk=pk)
    
    if request.method=='POST':
        if request.user == blog.author:
            title = request.POST.get('title')
            body = request.POST.get('body')
            blog.title = title
            blog.body = body
            blog.save()
        
            return redirect('blog_detail', blog.pk)
        
    return render(request, 'blog/blog_edit.html', {'blog': blog})

@login_required
def blog_delete(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('blog_list')
    
    
    
