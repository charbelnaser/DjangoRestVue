from django.urls import path, include, re_path
# from .views import MoviesList, MovieDetails
from .views import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')


urlpatterns = [
    path('', include(router.urls)),

]
# urlpatterns = [
#     path('movies', MoviesList.as_view()),
#     path('movies/<int:id>/', MovieDetails.as_view()),

# ]
