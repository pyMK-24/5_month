# movie_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.DirectorListAPIView.as_view()),  
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),  


    path('movies/', views.MovieListAPIView.as_view()), 
    path('movies/<int:id>/', views.MovieDetailAPIViewd.as_view()),  

 
    path('reviews/', views.ReviewListAPIView.as_view()), 
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),  
]
