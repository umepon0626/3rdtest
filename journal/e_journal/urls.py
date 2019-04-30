from django.urls import path
from . import views

app_name = 'e_journal'
urlpatterns = [
    path('', views.index, name='index'),
]
    