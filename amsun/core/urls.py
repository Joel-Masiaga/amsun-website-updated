from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('news/', views.NewsListView.as_view(), name='news-list'),
    path('events/', views.EventsListView.as_view(), name='events-list'),
    path('conference/', views.ConferenceView.as_view(), name='conference'),
    path('finalists-dinner/', views.FinalistsDinnerView.as_view(), name='finalists_dinner'),
    path('gazette/', views.GazetteView.as_view(), name='gazette'),
    path('alumni/', views.AlumniView.as_view(), name='alumni'),
    path('partners/', views.PartnersView.as_view(), name='partners'),
    path('leadership/', views.LeadershipView.as_view(), name='leadership'),
]