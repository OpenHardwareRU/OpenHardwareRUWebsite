from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    # ex: /homepage/
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
]