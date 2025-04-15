from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexV, name='indexURL'),
    path('one', views.oneV, name='oneURL'),
    path('two', views.twoV, name='twoURL'),

]