
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from app1 import views as v
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('studapi',v.StudApi,basename='studapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('refrashtoken/',TokenRefreshView.as_view()),
]
