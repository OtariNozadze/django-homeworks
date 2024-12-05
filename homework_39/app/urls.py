from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/add/', views.add_book, name='add_book' ),
    path('book/detail/<int:pk>/', views.book_details, name='book_details')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)