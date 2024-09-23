from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('create/',views.blog_create,name="blog_create"),
    path('<int:blog_id>/delete/',views.blog_delete,name="blog_delete"),
    path('<int:blog_id>/edit/',views.blog_edit,name="blog_edit"),
    path('register/',views.register,name="register"),
]
