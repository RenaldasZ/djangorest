from django.urls import path
from . import views

urlpatterns = [
    path('songlist', views.SongList.as_view()),
    path('bandlist', views.BandList.as_view()),
    path('', views.SongReviewList.as_view()),
    path('<int:pk>/', views.SongReviewDetail.as_view())
]