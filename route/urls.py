from page.views import *
from rest_framework import routers, serializers, viewsets

from django.urls import path, include

router = routers.DefaultRouter()


urlpatterns = [
    path('register', register),
    path('login', login),
    # path('table_post', .as_view()),
    path('fanlar', FanlarView.as_view()),

]

urlpatterns += router.urls
