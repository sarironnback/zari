from django.urls import path
from pages import views

urlpatterns = [
     path('', views.index, name='index'),
     path('detail/<slug:slug>/', views.creation_detail, name='detail'),
     path('about/', views.about, name='about'),
     path('contact/', views.contact, name='contact'),
     path('thankyou/', views.thankyou, name='thankyou')
]
