from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from api.views import BigThreeViewSet, UserViewSet, ManageUserView

router = routers.DefaultRouter()
router.register('bigthree', BigThreeViewSet)
router.register('users', UserViewSet)

urlpatterns =[
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls)),
]