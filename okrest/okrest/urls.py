from django.conf.urls import patterns, include, url

from django.contrib import admin
from api import views
admin.autodiscover()
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'headings', views.HeadingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)