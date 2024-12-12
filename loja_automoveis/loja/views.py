from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Carro, Cliente, Vendedor, Venda, Manutencao


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias/categoria_list.html'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categorias/categoria_detail.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categorias/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')

class CarroListView(ListView):
    model = Carro
    template_name = 'carro/carro_list.html'

class CarroDetailView(DetailView):
    model = Carro
    template_name = 'carro/carro_detail.html'

class CarroCreateView(CreateView):
    model = Carro
    fields = ['modelo', 'marca', 'preco', 'ano', 'categorias']
    template_name = 'carro/carro_form.html'
    success_url = reverse_lazy('carro_list')

class CarroUpdateView(UpdateView):
    model = Carro
    fields = ['modelo', 'marca', 'preco', 'ano', 'categorias']
    template_name = 'carro/carro_form.html'
    success_url = reverse_lazy('carro_list')

class CarroDeleteView(DeleteView):
    model = Carro
    template_name = 'carro/carro_confirm_delete.html'
    success_url = reverse_lazy('carro_list')

# Cliente CRUD
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone', 'endereco']
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone', 'endereco']
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')


class VendedorListView(ListView):
    model = Vendedor
    template_name = 'vendedores/vendedor_list.html'

class VendedorDetailView(DetailView):
    model = Vendedor
    template_name = 'vendedores/vendedor_detail.html'

class VendedorCreateView(CreateView):
    model = Vendedor
    fields = ['nome', 'especialidade']
    template_name = 'vendedores/vendedor_form.html'
    success_url = reverse_lazy('vendedor_list')

class VendedorUpdateView(UpdateView):
    model = Vendedor
    fields = ['nome', 'especialidade']
    template_name = 'vendedores/vendedor_form.html'
    success_url = reverse_lazy('vendedor_list')

class VendedorDeleteView(DeleteView):
    model = Vendedor
    template_name = 'vendedores/vendedor_confirm_delete.html'
    success_url = reverse_lazy('vendedor_list')


class VendaListView(ListView):
    model = Venda
    template_name = 'vendas/venda_list.html'

class VendaDetailView(DetailView):
    model = Venda
    template_name = 'vendas/venda_detail.html'

class VendaCreateView(CreateView):
    model = Venda
    fields = ['data', 'cliente', 'vendedor', 'carros'] 
    template_name = 'vendas/venda_form.html'
    success_url = reverse_lazy('venda_list')
    

class VendaUpdateView(UpdateView):
    model = Venda
    fields = ['data', 'cliente', 'vendedor', 'carros'] 
    template_name = 'vendas/venda_form.html'
    success_url = reverse_lazy('venda_list')

class VendaDeleteView(DeleteView):
    model = Venda
    template_name = 'vendas/venda_confirm_delete.html'
    success_url = reverse_lazy('venda_list')

class ManutencaoListView(ListView):
    model = Manutencao
    template_name = 'manutencoes/manutencao_list.html'

class ManutencaoDetailView(DetailView):
    model = Manutencao
    template_name = 'manutencoes/manutencao_detail.html'

class ManutencaoCreateView(CreateView):
    model = Manutencao
    fields = ['data', 'descricao', 'carro']
    template_name = 'manutencoes/manutencao_form.html'
    success_url = reverse_lazy('manutencao_list')

class ManutencaoUpdateView(UpdateView):
    model = Manutencao
    fields = ['data', 'descricao', 'carro']
    template_name = 'manutencoes/manutencao_form.html'
    success_url = reverse_lazy('manutencao_list')

class ManutencaoDeleteView(DeleteView):
    model = Manutencao
    template_name = 'manutencoes/manutencao_confirm_delete.html'
    success_url = reverse_lazy('manutencao_list')