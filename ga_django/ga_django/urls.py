# ga_django/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('ga_app.urls')),
]
