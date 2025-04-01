

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def my_view(request):
    return HttpResponse("Hello, world!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view),
]
