from django.urls import path

from.import views

urlpatterns = [
    path('', views.listaVacinados, name='list'),
]