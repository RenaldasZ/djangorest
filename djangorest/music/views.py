from rest_framework import generics
from . import models, serializers


class SongList(generics.ListAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer

