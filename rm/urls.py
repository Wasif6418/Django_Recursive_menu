from django.urls import path
from rm.views import MenuList
from . import views


urlpatterns = [
    path('menu/', views.MenuList.as_view(), name='menu-list'),

]
