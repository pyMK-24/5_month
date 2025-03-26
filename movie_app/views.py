from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models,serializers
from rest_framework import status
from django.db import transaction
from rest_framework import generics 

class DirectorListAPIView(generics.ListCreateAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer

class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    lookup_field = 'id'
      
class MovieListAPIView(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer

    def post(self, request, *args, **kwargs):
        validator = serializers.MovieValidateSerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,data=validator.errors)
        title = validator.validated_data.get('title')
        description = validator.validated_data.get('description')
        duration = validator.validated_data.get('duration')
        director_id = validator.validated_data.get('director_id')
        
        movie = models.Movie.objects.create(title=title,
                                                description=description,
                                                duration=duration,
                                                director_id=director_id
                                                )
        movie.save()
            
        return Response(data=serializers.MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)
    
class MovieDetailAPIViewd(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = 'id'
    
    def put(self, request, *args, **kwargs):
        movie_detail = self.get_object()
        validator = serializers.MovieValidateSerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,data=validator.errors)
        movie_detail.title = validator.validated_data.get('title')
        movie_detail.description = validator.validated_data.get('description')
        movie_detail.duration = validator.validated_data.get('duration')
        movie_detail.director_id = validator.validated_data.get('director_id')
        movie_detail.save()
        return Response(data=serializers.MovieSerializer(movie_detail).data,
                        status=status.HTTP_200_OK)

class ReviewListAPIView(generics.ListCreateAPIView):     
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def post(self, request, *args, **kwargs):
        validator = serializers.ReviewValidateSerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,data=validator.errors)
        text = validator.validated_data.get('text')
        movie_id = validator.validated_data.get('movie_id')
        stars = validator.validated_data.get('stars')
        
        review = models.Review.objects.create(text=text,
                                                  movie_id=movie_id,
                                                  stars=stars)
        review.save()
        return Response(data=serializers.ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)
 
class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        review_detail = self.get_object()
        validator = serializers.ReviewValidateSerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,data=validator.errors)
        review_detail.text = validator.validated_data.get('text')
        review_detail.movie_id = validator.validated_data.get('movie_id')
        review_detail.stars = validator.validated_data.get('stars')
        review_detail.save()
        return Response(data=serializers.ReviewSerializer(review_detail).data,status=status.HTTP_200_OK)