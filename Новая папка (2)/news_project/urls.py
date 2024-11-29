from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import NewsViewSet, CategoryViewSet, TagViewSet
from django.contrib import admin
from django.urls import path

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('categories', CategoryViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]