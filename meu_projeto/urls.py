# meu_projeto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),  # Incluindo as URLs do aplicativo de produtos
]