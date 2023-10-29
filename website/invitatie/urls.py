from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact_view, name='contact_view'),

]