# MODULOS E PACOTES NECESSARIOS PARA I
from django.contrib import admin
from django.urls import path, include

# ROTAS DA APLICAÇÃO 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]
