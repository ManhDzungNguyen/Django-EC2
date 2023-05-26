from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.cv, name='cv'),
    path('cv1', views.cv1, name='cv1'),
    path('download/', views.download_file, name='download_file'),
]