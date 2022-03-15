from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply', views.apply, name='apply'),
    path('application', views.application, name='application'),
    path('viewapplications/<id>', views.viewapplication, name='details')
]
