from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'grade', 'movie']


class MovieSerializer(serializers.ModelSerializer):
    # Show actors as nested data
    actors = ActorSerializer(many=True, read_only=True)
    # Optional: show related reviews too
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'actors', 'reviews']



