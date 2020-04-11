from django.conf.urls import url
from django.urls import include
from users import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.MainViewSet, base_name='MainViewSet'),

urlpatterns = [
    url(r'^', include(router.urls)),
]