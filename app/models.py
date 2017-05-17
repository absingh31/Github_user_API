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

    def __unicode__(self): #Python2 declaration
        return (str(self.name + str(self.user_id)))

