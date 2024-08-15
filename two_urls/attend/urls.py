from django.urls import path
from attend import views
urlpatterns=[
    path('<str:name>',views.attend)] 