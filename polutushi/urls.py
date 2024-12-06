from django.urls import path
from . import views

app_name = 'polutushi'

urlpatterns = [
    path('<int:id>/', views.polutushi_detail, name='polutushi_detail'),
]
