from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def doctor_blog_create(request):
    if request.user.user_type != 'doctor':
        return redirect('home')

    form = BlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('doctor_blog_list')

    return render(request, 'blog/doctor_blog_create.html', {'form': form})

@login_required
def doctor_blog_list(request):
    if request.user.user_type != 'doctor':
        return redirect('home')
    blogs = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/doctor_blog_list.html', {'blogs': blogs})

@login_required
def patient_blog_list(request):
    blogs_by_category = {}
    for cat, _ in BlogPost.CATEGORIES:
      blogs = BlogPost.objects.filter(category=cat, is_draft=False)
      blogs_by_category[cat] = blogs
    return render(request, 'blog/patient_blog_list.html', {'blogs_by_category': blogs_by_category})
