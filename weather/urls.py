from django.urls import path, include, re_path
from . import views

urlpatterns = [
    #re_path(r'^(?P<pk>\d+)', views.get_delete_update_city, name = 'cool')
    path('', views.index, name='index'),
    re_path(r'^city/(?P<name>[\w]+)$', views.get_city_by_name, name = 'get_city_by_name'),
    path('cities/', views.get_cities, name = 'get_cities'),
    path('populate_db/', views.populate_db, name = 'populate_db')
]