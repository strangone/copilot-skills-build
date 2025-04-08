from djongo import models
from djongo.models import ObjectIdField
from bson import ObjectId

class User(models.Model):
    _id = ObjectIdField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

def generate_unique_object_id():
    return ObjectId()

class Team(models.Model):
    _id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = ObjectIdField(primary_key=True, default=generate_unique_object_id)  # Ensure unique default values
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Temporarily allow null values
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} by {self.user.username}"

class Leaderboard(models.Model):
    _id = ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.team.name}: {self.score}"

class Workout(models.Model):
    _id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name
