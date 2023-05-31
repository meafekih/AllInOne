from django.contrib import admin
from django.urls import path, include
from .views import blogApi
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blog', blogApi)

urlpatterns = [
    path('', include(router.urls)),
]
