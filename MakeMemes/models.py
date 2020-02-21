from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# creating a new model.
class Post(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True)

    text = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now=True)
    vote = models.IntegerField(default=0)

    # display the name of the object instead of object1, object2 and so on.
    def __str__(self):
        # return str('name: ' + str(self.text) + ' user: ' + str(self.user))
        return self.text

class Search(models.Model):
    search = models.CharField(max_length=256)

    # display the name of the object instead of object1, object2 and so on.
    def __str__(self):
        return self.search
