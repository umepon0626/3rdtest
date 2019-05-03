from django.urls import path
from . import views

app_name = 'E_journal'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:content_id>/',views.detail,name='detail'),
    path('new_journal/',views.new_journal,name='new_journal'),
    path('delete_journal/<int:content_id>', views.delete_journal, name='delete_journal'),
    path('edit_journal/<int:content_id>',views.edit_journal, name = 'edit_journal')
]
    