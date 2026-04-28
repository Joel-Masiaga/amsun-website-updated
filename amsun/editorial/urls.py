from django.urls import path
from . import views

app_name = 'editorial'

urlpatterns = [
    # Auth
    path('login/',  views.editorial_login,  name='login'),
    path('logout/', views.editorial_logout, name='logout'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Blogs
    path('blogs/',                   views.blog_list,   name='blog-list'),
    path('blogs/create/',            views.blog_create, name='blog-create'),
    path('blogs/<int:pk>/edit/',     views.blog_edit,   name='blog-edit'),
    path('blogs/<int:pk>/delete/',   views.blog_delete, name='blog-delete'),

    # News
    path('news/',                    views.news_list,   name='news-list'),
    path('news/create/',             views.news_create, name='news-create'),
    path('news/<int:pk>/edit/',      views.news_edit,   name='news-edit'),
    path('news/<int:pk>/delete/',    views.news_delete, name='news-delete'),

    # Events
    path('events/',                  views.event_list,   name='event-list'),
    path('events/create/',           views.event_create, name='event-create'),
    path('events/<int:pk>/edit/',    views.event_edit,   name='event-edit'),
    path('events/<int:pk>/delete/',  views.event_delete, name='event-delete'),

    # Research (admin only)
    path('research/',                    views.research_list,   name='research-list'),
    path('research/create/',             views.research_create, name='research-create'),
    path('research/<int:pk>/edit/',      views.research_edit,   name='research-edit'),
    path('research/<int:pk>/delete/',    views.research_delete, name='research-delete'),

    # Users (admin only)
    path('users/',                   views.user_list,   name='user-list'),
    path('users/create/',            views.user_create, name='user-create'),
    path('users/<int:pk>/delete/',   views.user_delete, name='user-delete'),
]
