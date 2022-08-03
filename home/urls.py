from rest_framework import routers

from django.contrib import admin
from django.urls import path, include
from page.views import *

router = routers.DefaultRouter()
router.register(r'table', TableViewSet)
router.register(r'table_post', GroupDayView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("route.urls")),
    path('api/register', register),
    path('api/login', login),

]
urlpatterns += router.urls
