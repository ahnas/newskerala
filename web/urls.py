from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('news/<str:slug>/', views.post,name="post"),
    path('video/<str:slug>/', views.video,name="video"),
    path('category/<str:slug>/', views.category,name="category"),
    path('tag/<str:tag>/', views.tagged_news,name="tagged_news"),
    path('announcements/', views.announcements,name="announcements"),
    path('gallery/', views.gallery,name="gallery"),
    path('about/', views.about,name="about"),
    path('advertisement/', views.advertisement,name="advertisement"),
    path('join_whatsapp/', views.join_whatsapp,name="join_whatsapp"),
    path('policy/', views.policy,name="policy"),
    path('terms/', views.terms,name="terms"),
    path('disclaimer/', views.disclaimer,name="disclaimer"),
    path('contact/', views.contact,name="contact"),
    path('newsletter/', views.newsletter,name="newsletter"),
]
