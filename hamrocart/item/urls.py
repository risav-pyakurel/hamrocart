from django.urls import path

from.import views

from . import views

app_name = 'item'

urlpatterns =[
  path('<int:pk>/', views.detail, name='detail')

]