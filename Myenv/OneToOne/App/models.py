from django.db import models
from django.db.models import Q


class Singer(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    def __str__(self):
        return self.Name+" ID "+str(self.id)

class Song(models.Model):
    singer = models.OneToOneField(Singer, on_delete=models.CASCADE, primary_key=True, limit_choices_to=Q(id=1) | Q(id=4))
    song_name = models.CharField(max_length=200)
    song_publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.song_name

# superuser:  username and password == admin