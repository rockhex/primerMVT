
from django.contrib import admin
from django.urls import path
from .views import mostrar_familia


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_familia),
    
]
