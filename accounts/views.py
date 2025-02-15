from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from posts.models import Post
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your views here.

@login_required
def account(request):
    user_posts = Post.objects.filter(author=request.user).order_by('-pub_date')
    return render(request, 'account/account.html', {
        'user_posts': user_posts
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'account/edit_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')
