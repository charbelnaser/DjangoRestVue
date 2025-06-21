from django.urls import path, include, re_path
# from .views import MoviesList, MovieDetails
from .views import MovieViewSet,ActorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('actors', ActorViewSet, basename='actors')



urlpatterns = [
    path('', include(router.urls)),

]