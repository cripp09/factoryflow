from django.urls import path
from . import views

app_name = 'polutushi'

urlpatterns = [
    path('delete/<int:id>/', views.polutushi_delete, name='polutushi_delete'),
    path('update/<int:id>/', views.polutushi_update, name='polutushi_update'),
    path('date/', views.polutushi_list_with_date, name='polutushi_list_with_date'),
    path('<int:id>/', views.polutushi_detail, name='polutushi_detail'),
    path('', views.polutushi_list_all, name='polutushi_list_all'),
]
