from django.urls import path, include
from .views import MovieViewSet, ActorViewSet, ReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('actors', ActorViewSet, basename='actors')
router.register('reviews', ReviewViewSet, basename='reviews')




urlpatterns = [
    path('', include(router.urls)),

]