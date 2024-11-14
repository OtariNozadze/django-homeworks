from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/add/', views.add_book, name='add_book' ),
]