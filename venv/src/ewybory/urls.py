from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('register', views.WyborcyView)
router.register('logowanie', views.KandydaciView)


urlpatterns = [
    path('', include(router.urls)),
]