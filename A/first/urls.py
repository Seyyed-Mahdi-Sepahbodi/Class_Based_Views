from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'first'
urlpatterns = [
    # path('', views.home, name='home'),

    # path('', TemplateView.as_view(template_name='first/home.html'), name='home'), # this is for making static pages
    path('', views.Home.as_view(), name='home'),

    path('create/', views.TodoCreateView.as_view(), name='todo_create'),

    # path('<int:pk>/', views.DetailTodo.as_view(), name='detail_todo'),
    path('<slug:myslug>/', views.DetailTodo.as_view(), name='detail_todo'),

]
