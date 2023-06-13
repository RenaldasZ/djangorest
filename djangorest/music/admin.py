from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Band)
admin.site.register(models.Song)
admin.site.register(models.SongReview)
admin.site.register(models.SongReviewComment)
admin.site.register(models.SongReviewLike)