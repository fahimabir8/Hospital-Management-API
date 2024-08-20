from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() #wifi router
 
router.register('',views.AppointmentViewSet) # antena ready

urlpatterns = [
    path('',include(router.urls)),
]
