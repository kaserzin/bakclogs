from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/create/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/<int:pk>/update/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),

    path('carros/', views.CarroListView.as_view(), name='carro_list'),
    path('carros/create/', views.CarroCreateView.as_view(), name='carro_create'),
    path('carros/<int:pk>/', views.CarroDetailView.as_view(), name='carro_detail'),
    path('carros/<int:pk>/update/', views.CarroUpdateView.as_view(), name='carro_update'),
    path('carros/<int:pk>/delete/', views.CarroDeleteView.as_view(), name='carro_delete'),

    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/create/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<int:pk>/update/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    path('vendedores/', views.VendedorListView.as_view(), name='vendedor_list'),
    path('vendedores/create/', views.VendedorCreateView.as_view(), name='vendedor_create'),
    path('vendedores/<int:pk>/', views.VendedorDetailView.as_view(), name='vendedor_detail'),
    path('vendedores/<int:pk>/update/', views.VendedorUpdateView.as_view(), name='vendedor_update'),
    path('vendedores/<int:pk>/delete/', views.VendedorDeleteView.as_view(), name='vendedor_delete'),

    path('vendas/', views.VendaListView.as_view(), name='venda_list'),
    path('vendas/create/', views.VendaCreateView.as_view(), name='venda_create'),
    path('vendas/<int:pk>/', views.VendaDetailView.as_view(), name='venda_detail'),
    path('vendas/<int:pk>/update/', views.VendaUpdateView.as_view(), name='venda_update'),
    path('vendas/<int:pk>/delete/', views.VendaDeleteView.as_view(), name='venda_delete'),

    path('manutencoes/', views.ManutencaoListView.as_view(), name='manutencao_list'),
    path('manutencoes/create/', views.ManutencaoCreateView.as_view(), name='manutencao_create'),
    path('manutencoes/<int:pk>/', views.ManutencaoDetailView.as_view(), name='manutencao_detail'),
    path('manutencoes/<int:pk>/update/', views.ManutencaoUpdateView.as_view(), name='manutencao_update'),
    path('manutencoes/<int:pk>/delete/', views.ManutencaoDeleteView.as_view(), name='manutencao_delete'),
]
