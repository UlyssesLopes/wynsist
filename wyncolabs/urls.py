"""wyncolabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modulos/colaboradores/', views.lista_colaboradores),
    path('modulos/colaboradores/todoscolaboradores/novocolaborador/', views.novocolaborador),
    path('modulos/colaboradores/todoscolaboradores/novocolaborador/submit', views.submit_novocolaborador),
    path('modulos/colaboradores/novocolaborador/delete/<int:id_evento>/', views.delete_colaborador),
    path('modulos/colaboradores/todoscolaboradores/', views.todos_colaboradores),
    path('modulos/colaboradores/todoscolaboradores/dados/<int:id_evento>/', views.dados_colaborador),    
    path('modulos/colaboradores/todoscolaboradores/dados/<int:id_evento>/alelo/', views.adicionar_alelo),
    path('modulos/colaboradores/todoscolaboradores/dados/<int:id_evento>/alelo/submit', views.submit_alelo),
    path('modulos/colaboradores/todoscolaboradores/dados/<int:id_evento>/pagamento/', views.adicionar_pagamento),
    path('modulos/colaboradores/todoscolaboradores/dados/<int:id_evento>/pagamento/submit', views.submit_pagamento),
    path('', RedirectView.as_view(url='/modulos/colaboradores/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('todos/', views.todos_colaboradores),
    path('modulos/', views.modulos),
    path('modulos/contratos/', views.contratos),
]
