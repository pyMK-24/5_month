from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models,serializers
from rest_framework import status
from django.db import transaction

@api_view(http_method_names=['GET','POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors = models.Director.objects.all()
        serializer = serializers.DirectorSerializer(instance=directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        print(name)
        
        with transaction.atomic():
            director = models.Director.objects.create(name=name)
            director.save()
        
        return Response(data=serializers.DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED) 

@api_view(['GET','PUT','DELETE'])
def director_detail_api_view(request,id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(data={'Error': 'Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name= request.data.get('name')
        director.save()
        return Response(data=serializers.DirectorSerializer(director).data,status=status.HTTP_201_CREATED)
        
@api_view(http_method_names=['GET','POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        serializer = serializers.MovieSerializer(instance=movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        
        
        with transaction.atomic():
            movie = models.Movie.objects.create(title=title,
                                                description=description,
                                                duration=duration,
                                                director_id=director_id
                                                )
            movie.save()
            
        return Response(data=serializers.MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def movie_detail_api_view(request,id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(data={'Error':'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=serializers.MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)
        
@api_view(http_method_names=['GET','POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = models.Review.objects.all()
        serializer = serializers.ReviewSerializer(instance=reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        
        with transaction.atomic():
            review = models.Review.objects.create(text=text,
                                                  movie_id=movie_id,
                                                  stars=stars)
        
        return Response(data=serializers.ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def review_detail_api_view(request,id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(data={'Error':'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = serializers.ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=serializers.ReviewSerializer(review).data,status=status.HTTP_201_CREATED)