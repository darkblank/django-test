from django.shortcuts import render, redirect

from post.forms import PostForm
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            photo = form.cleaned_data['photo']
            content = form.cleaned_data['content']
            Post.objects.create(
                title=title,
                photo=photo,
                content=content,
            )
            return redirect('post_list')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'post/post_create.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        post.delete()
    return redirect('post_list')
