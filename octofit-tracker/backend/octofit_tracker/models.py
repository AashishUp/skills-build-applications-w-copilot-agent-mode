from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.name}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - Rank {self.rank}"

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.name
