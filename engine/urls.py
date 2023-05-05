from django.urls import path
from . import views
app_name = 'engine'


urlpatterns = [
    path('', views.homeView, name='homeURL'),
    path('/teachers', views.teachersView, name='teachersURL'),
]

