
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls', namespace='app')),
    path('users/', include('users.urls', namespace='users')),
    path('users/', include('django.contrib.auth.urls'))

]
