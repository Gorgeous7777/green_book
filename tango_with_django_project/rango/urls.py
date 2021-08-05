from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/<page_id>/', views.show_page, name='show_page'),
    path('category/<slug:category_name_slug>/<page_id>/add_like/', views.add_like, name='add_like'),
    path('restricted/', views.restricted, name='restricted'),
    path('search/', views.search, name='search'),
    path('categories/', views.show_categories, name='show_categories'),

]