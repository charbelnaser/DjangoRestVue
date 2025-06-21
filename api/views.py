from django.shortcuts import render, HttpResponse
from .models import Movie
from .serializers import MovieSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics, mixins
# Create your views here.
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



# class MovieViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, 
#                    mixins.CreateModelMixin, mixins.RetrieveModelMixin, 
#                    mixins.DestroyModelMixin, mixins.UpdateModelMixin):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer



# class MovieViewSet(viewsets.ViewSet):

#     def list(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return  Response(serializer.data)
    
#     def create(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         queryset = Movie.objects.all()
#         movie = get_object_or_404(queryset, pk=pk)
#         serializer = MovieSerializer(movie)
#         return  Response(serializer.data)

#     def update(self, request, pk=None):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







# class MoviesList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)

# class MovieDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):

#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     lookup_field = 'id'

#     def get(self, request, id):
#         return self.retrieve(request, id=id)
    
#     def put(self, request, id):
#         return self.update(request, id=id)

#     def delete(self, request, id):
#         return self.destroy(request, id=id)

# class MoviesList(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class MovieDetails(APIView):
#     def get_object(self, id):
#         try:
#             return Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, id):
#         movie = self.get_object(id)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     def put(self, request, id):
#         movie = self.get_object(id)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         movie = self.get_object(id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT', 'DELETE'])
# def movie_detail(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
   
