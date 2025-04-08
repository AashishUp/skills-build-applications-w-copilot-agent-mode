from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserAPITestCase(APITestCase):
    def test_create_user(self):
        data = {"email": "test@example.com", "name": "Test User", "age": 25}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamAPITestCase(APITestCase):
    def test_create_team(self):
        data = {"name": "Team A", "members": []}
        response = self.client.post("/api/teams/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityAPITestCase(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        data = {"user": user.id, "activity_type": "Running", "duration": 30, "calories_burned": 200, "date": "2025-04-08"}
        response = self.client.post("/api/activity/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardAPITestCase(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team A")
        data = {"team": team.id, "points": 100, "rank": 1}
        response = self.client.post("/api/leaderboard/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutAPITestCase(APITestCase):
    def test_create_workout(self):
        data = {"name": "Workout A", "description": "Test workout", "duration": 30, "difficulty": "Easy"}
        response = self.client.post("/api/workouts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
