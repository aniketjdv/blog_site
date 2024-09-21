from django.urls import path,include
from api.views import BlogViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'blogs',BlogViewset)


urlpatterns = [
    path('', include(router.urls)),
]