from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from MakeMemes.models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created')

    return render(request, 'SocialMedia/index.html', {
        'posts': posts
    })

def add_post(request):
    current_date = timezone.now()
    content = request.POST['new_post']

    Post.objects.create(text=content, created=current_date, user=request.user)

    return HttpResponseRedirect("/home")

def profile(request):
    posts = Post.objects.all().order_by('-created')

    return render(request, 'SocialMedia/profile.html', {
        'posts': posts,
        'name': request.user
    })

def vote(request, id_post):
    if request.method == 'POST':
        if request.POST.get('vote_up'):
            post = Post.objects.get(id=id_post)
            post.vote += 1
            post.save()
            return HttpResponseRedirect('/home')

        else:
            post = Post.objects.get(id=id_post)
            post.vote -= 1
            post.save()
            return HttpResponseRedirect('/home')


