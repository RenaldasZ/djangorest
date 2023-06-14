from django.urls import path
from . import views

urlpatterns = [
    path('', views.SongList.as_view()),
    path('bandlist', views.BandList.as_view()),
    path('bandlist/<int:pk>/', views.BandDetail.as_view()),
    path('song_reviews/', views.SongReviewList.as_view()),
    path('song_reviews/<int:pk>/', views.SongReviewDetail.as_view()),
    path('song_reviews/<int:pk>/like', views.SongReviewCreateDestroy.as_view()),
    path('song_reviews/<int:song_pk>/comments/', views.SongReviewCommentList.as_view()),
    path('comment/<int:pk>/', views.SongReviewCommentDetail.as_view()),
]