from django.shortcuts import render
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
