from django.urls import path
from app1 import views
urlpatterns=[
    path('<int:p>/<int:t>/<int:r>',views.one),
] 