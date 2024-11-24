from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.criar_produto, name='criar_produto'),
    path('<int:id>/editar/', views.editar_produto, name='editar_produto'),
    path('<int:id>/excluir/', views.excluir_produto, name='excluir_produto'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('', views.lista_produtos, name='produtos_lista'),
]
