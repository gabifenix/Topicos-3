from django.urls import path
from.import views

urlpatterns = [
    path('', views.listaVacinados, name='vacinados-list'),
    path('cadastro/<int:id>', views.cadastroView, name="cadastro-view"),
    path('novocadastro/', views.novoCadastro, name="novo-cadastro"),
    path('edit/<int:id>', views.editCadastro, name="edit-cadastro"),
    path('delete/<int:id>', views.deleteCadastro, name="delete-cadastro"),
]