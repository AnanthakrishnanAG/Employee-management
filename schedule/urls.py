from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('users',views.EmpView, basename='users')
router.register('periods',views.ActivityPeriodView, basename='periods')




urlpatterns=[
    
    path('',include(router.urls)),
  
]