from django.urls import path, include
from employee import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'log', views.LogViewSet)


urlpatterns = [
    path('', views.home, name="home"),
    path('api/', include(router.urls)),
]