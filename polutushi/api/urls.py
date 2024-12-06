from django.urls import path
from . import views

app_name = 'polutushi'

urlpatterns = [
    path('polutushi/',
        views.PolutushiListView.as_view(),
        name='subject_list'),
    path('polutushi/add/',
        views.PolutushaAddView.as_view(),
        name='polutushi_add'),
    path('polutushi/<pk>/',
        views.PolutushiDetailView.as_view(),
        name='subject_detail'),

]  