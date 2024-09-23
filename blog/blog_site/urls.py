from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('create/',views.blog_create,name="blog_create"),
    path('delete/',views.blog_delete,name="blog_delete"),
]
