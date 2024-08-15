from django.urls import path
from app2 import views
urlpatterns=[
    path('1',views.one),
    path('k',views.two)
]