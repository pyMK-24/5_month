from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()
    class Meta:
        model = models.Director
        fields = ('id','name','movie_count')
        
    def get_movie_count(self, director):
        return director.movies.count()
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ('id','text','movie','stars')
       
class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = models.Movie
        fields = ('id','title','description','duration','director','reviews','average_rating')

    def get_average_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            sum_reviews = sum(review.stars for review in reviews)
            average = sum_reviews / len(reviews)
            return average
        return None
        
class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,min_length=1,max_length=100)

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True,min_length=1,max_length=1000)
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    
    def validate_movie_id(self, movie_id):
        if not models.Review.objects.filter(movie_id=movie_id).exists():
            raise ValidationError('Movie is not exist')
        return movie_id
    
class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True,min_length=1,max_length=200)
    description = serializers.CharField()
    duration = serializers.FloatField(min_value=1, max_value=1000000)
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        if not models.Movie.objects.filter(director_id=director_id).exists():
            raise ValidationError('Director is not exist')
        return director_id
        
