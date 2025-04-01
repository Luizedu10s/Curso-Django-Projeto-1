# MODULOS E PACOTES NECESSARIOS PARA O APP 

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from recipes.views import my_view, home, about

# ROTAS DA APLICAÇÃO 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view),
    path('home/', home),
    path('about/', about),
]
