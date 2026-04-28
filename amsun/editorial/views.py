from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse

from core.models import Blog, News, Events, Research
from users.models import User

from .decorators import editorial_login_required, admin_required
from .forms import (
    BlogForm, NewsForm, EventForm, ResearchForm,
    EditorCreateForm, EditorialLoginForm,
)


# ─────────────────────────────────────────────────────────────────────────────
# Auth
# ─────────────────────────────────────────────────────────────────────────────

def editorial_login(request):
    if request.user.is_authenticated and request.user.role in ('editor', 'admin'):
        return redirect('editorial:dashboard')
    if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
        return redirect('editorial:dashboard')

    form = EditorialLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email    = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user     = authenticate(request, email=email, password=password)
        if user is not None:
            if user.role in ('editor', 'admin') or user.is_staff or user.is_superuser:
                login(request, user)
                return redirect('editorial:dashboard')
            else:
                messages.error(request, 'You do not have editorial access.')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'editorial/login.html', {'form': form})


def editorial_logout(request):
    logout(request)
    return redirect('editorial:login')


# ─────────────────────────────────────────────────────────────────────────────
# Dashboard
# ─────────────────────────────────────────────────────────────────────────────

@editorial_login_required
def dashboard(request):
    is_admin = (
        request.user.role == 'admin'
        or request.user.is_staff
        or request.user.is_superuser
    )
    stats = {
        'blogs':    Blog.objects.count(),
        'news':     News.objects.count(),
        'events':   Events.objects.count(),
        'research': Research.objects.count(),
    }
    recent_blogs  = Blog.objects.order_by('-created_at')[:5]
    recent_news   = News.objects.order_by('-published_date')[:5]
    recent_events = Events.objects.order_by('-date')[:5]

    users_count = User.objects.count() if is_admin else None

    return render(request, 'editorial/dashboard.html', {
        'stats': stats,
        'recent_blogs':  recent_blogs,
        'recent_news':   recent_news,
        'recent_events': recent_events,
        'users_count':   users_count,
        'is_admin':      is_admin,
    })


# ─────────────────────────────────────────────────────────────────────────────
# Blogs
# ─────────────────────────────────────────────────────────────────────────────

@editorial_login_required
def blog_list(request):
    blogs    = Blog.objects.order_by('-created_at')
    is_admin = _is_admin(request.user)
    return render(request, 'editorial/blog_list.html', {'blogs': blogs, 'is_admin': is_admin})


@editorial_login_required
def blog_create(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Blog post created successfully.')
        return redirect('editorial:blog-list')
    return render(request, 'editorial/blog_form.html', {
        'form': form, 'action': 'Create', 'content_type': 'Blog Post',
        'is_admin': _is_admin(request.user),
    })


@editorial_login_required
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Blog post updated.')
        return redirect('editorial:blog-list')
    return render(request, 'editorial/blog_form.html', {
        'form': form, 'action': 'Edit', 'content_type': 'Blog Post', 'obj': blog,
        'is_admin': _is_admin(request.user),
    })


@editorial_login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog post deleted.')
        return redirect('editorial:blog-list')
    return render(request, 'editorial/confirm_delete.html', {
        'obj': blog, 'obj_name': blog.title,
        'content_type': 'Blog Post',
        'cancel_url': reverse('editorial:blog-list'),
        'is_admin': _is_admin(request.user),
    })


# ─────────────────────────────────────────────────────────────────────────────
# News
# ─────────────────────────────────────────────────────────────────────────────

@editorial_login_required
def news_list(request):
    news     = News.objects.order_by('-published_date')
    is_admin = _is_admin(request.user)
    return render(request, 'editorial/news_list.html', {'news': news, 'is_admin': is_admin})


@editorial_login_required
def news_create(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'News article created.')
        return redirect('editorial:news-list')
    return render(request, 'editorial/news_form.html', {
        'form': form, 'action': 'Create', 'content_type': 'News Article',
        'is_admin': _is_admin(request.user),
    })


@editorial_login_required
def news_edit(request, pk):
    article = get_object_or_404(News, pk=pk)
    form    = NewsForm(request.POST or None, request.FILES or None, instance=article)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'News article updated.')
        return redirect('editorial:news-list')
    return render(request, 'editorial/news_form.html', {
        'form': form, 'action': 'Edit', 'content_type': 'News Article', 'obj': article,
        'is_admin': _is_admin(request.user),
    })


@editorial_login_required
def news_delete(request, pk):
    article = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'News article deleted.')
        return redirect('editorial:news-list')
    return render(request, 'editorial/confirm_delete.html', {
        'obj': article, 'obj_name': article.headline,
        'content_type': 'News Article',
        'cancel_url': reverse('editorial:news-list'),
        'is_admin': _is_admin(request.user),
    })


# ─────────────────────────────────────────────────────────────────────────────
# Events
# ─────────────────────────────────────────────────────────────────────────────

@editorial_login_required
def event_list(request):
    events   = Events.objects.order_by('-date')
    is_admin = _is_admin(request.user)
    return render(request, 'editorial/event_list.html', {'events': events, 'is_admin': is_admin})


@editorial_login_required
def event_create(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Event created.')
        return redirect('editorial:event-list')
    return render(request, 'editorial/event_form.html', {
        'form': form, 'action': 'Create', 'content_type': 'Event',
        'is_admin': _is_admin(request.user),
    })


@editorial_login_required
def event_edit(request, pk):
    event = get_object_or_404(Events, pk=pk)
    form  = EventForm(request.POST or None, request.FILES or None, instance=event)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Event updated.')
        return redirect('editorial:event-list')
    return render(request, 'editorial/event_form.html', {
        'form': form, 'action': 'Edit', 'content_type': 'Event', 'obj': event,
        'is_admin': _is_admin(request.user),
    })


@editorial_login_required
def event_delete(request, pk):
    event = get_object_or_404(Events, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted.')
        return redirect('editorial:event-list')
    return render(request, 'editorial/confirm_delete.html', {
        'obj': event, 'obj_name': event.title,
        'content_type': 'Event',
        'cancel_url': reverse('editorial:event-list'),
        'is_admin': _is_admin(request.user),
    })


# ─────────────────────────────────────────────────────────────────────────────
# Research  (admin only)
# ─────────────────────────────────────────────────────────────────────────────

@admin_required
def research_list(request):
    articles = Research.objects.order_by('-published_date')
    return render(request, 'editorial/research_list.html', {
        'articles': articles, 'is_admin': True,
    })


@admin_required
def research_create(request):
    form = ResearchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Research article added.')
        return redirect('editorial:research-list')
    return render(request, 'editorial/research_form.html', {
        'form': form, 'action': 'Create', 'content_type': 'Research',
        'is_admin': True,
    })


@admin_required
def research_edit(request, pk):
    article = get_object_or_404(Research, pk=pk)
    form    = ResearchForm(request.POST or None, instance=article)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Research article updated.')
        return redirect('editorial:research-list')
    return render(request, 'editorial/research_form.html', {
        'form': form, 'action': 'Edit', 'content_type': 'Research', 'obj': article,
        'is_admin': True,
    })


@admin_required
def research_delete(request, pk):
    article = get_object_or_404(Research, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Research article deleted.')
        return redirect('editorial:research-list')
    return render(request, 'editorial/confirm_delete.html', {
        'obj': article, 'obj_name': article.title,
        'content_type': 'Research',
        'cancel_url': reverse('editorial:research-list'),
        'is_admin': True,
    })


# ─────────────────────────────────────────────────────────────────────────────
# User Management  (admin only)
# ─────────────────────────────────────────────────────────────────────────────

@admin_required
def user_list(request):
    users = User.objects.order_by('-date_joined')
    return render(request, 'editorial/user_list.html', {
        'users': users, 'is_admin': True,
    })


@admin_required
def user_create(request):
    form = EditorCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'User {form.cleaned_data["email"]} created.')
        return redirect('editorial:user-list')
    return render(request, 'editorial/user_form.html', {
        'form': form, 'action': 'Create', 'is_admin': True,
    })


@admin_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user == request.user:
        messages.error(request, 'You cannot delete your own account.')
        return redirect('editorial:user-list')
    if request.method == 'POST':
        email = user.email
        user.delete()
        messages.success(request, f'User {email} deleted.')
        return redirect('editorial:user-list')
    return render(request, 'editorial/confirm_delete.html', {
        'obj': user, 'obj_name': user.email,
        'content_type': 'User',
        'cancel_url': reverse('editorial:user-list'),
        'is_admin': True,
    })


# ─────────────────────────────────────────────────────────────────────────────
# Helper
# ─────────────────────────────────────────────────────────────────────────────

def _is_admin(user):
    return user.role == 'admin' or user.is_staff or user.is_superuser
