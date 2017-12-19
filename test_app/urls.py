from django.urls import path

from . import views

app_name = 'test_app'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /test_app/5/
    path('get/', views.get, name='get'),
]
