from django.urls import path
from recipes.views import my_view, home, about

# ROTAS DA APLICAÇÃO 

urlpatterns = [
    path('', my_view),
    path('home/', home),
    path('about/', about),
]
