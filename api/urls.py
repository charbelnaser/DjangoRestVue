from django.urls import path
from .views import MoviesList, MovieDetails

urlpatterns = [
    path('movies', MoviesList.as_view()),
    path('movies/<int:id>/', MovieDetails.as_view()),

]
