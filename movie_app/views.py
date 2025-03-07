from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models,serializers
from rest_framework import status

@api_view(http_method_names=['GET'])
def director_list_api_view(request):
    directors = models.Director.objects.all()
    serializer = serializers.DirectorSerializer(instance=directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_detail_api_view(request,id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(data={'Error': 'Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = serializers.DirectorDetailSerializer(director).data
    return Response(data=data)
    
@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movies = models.Movie.objects.all()
    serializer = serializers.MovieDetailSerializer(instance=movies, many=True)
    return Response(data=serializer.data)
    
@api_view(['GET'])
def movie_detail_api_view(request,id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(data={'Error':'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = serializers.MovieDetailSerializer(movie).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = models.Review.objects.all()
    serializer = serializers.ReviewSerializer(instance=reviews, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_detail_api_view(request,id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(data={'Error':'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = serializers.ReviewDetailSerializer(review).data
    return Response(data=data)