from django.db import models
# Create your models here.

class User_info(models.Model):
    user_id = models.PositiveIntegerField()
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=250, blank=True, null=True)
    public_gists = models.PositiveIntegerField()
    public_repos = models.PositiveIntegerField()
    followers = models.PositiveIntegerField()
    following = models.PositiveIntegerField()
    date_searched = models.DateField()
    image_for_thumbnail = models.CharField(max_length=500, default='Well..')

    def Thumbnail(self):
        return '<img src="%s" width="30" height="30"/>' % self.image_for_thumbnail
    Thumbnail.allow_tags = True



