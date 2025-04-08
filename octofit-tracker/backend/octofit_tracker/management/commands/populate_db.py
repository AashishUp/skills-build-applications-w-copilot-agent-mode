from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(_id=ObjectId(), name='Blue Team', members=[users[0], users[1]]),
            Team(_id=ObjectId(), name='Gold Team', members=[users[2], users[3], users[4]]),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=60, calories_burned=500, date='2025-04-08'),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=90, calories_burned=700, date='2025-04-07'),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=45, calories_burned=400, date='2025-04-06'),
            Activity(_id=ObjectId(), user=users[3], activity_type='Swimming', duration=30, calories_burned=300, date='2025-04-05'),
            Activity(_id=ObjectId(), user=users[4], activity_type='Strength Training', duration=120, calories_burned=800, date='2025-04-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=teams[0], points=150, rank=1),
            Leaderboard(_id=ObjectId(), team=teams[1], points=120, rank=2),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Endurance cycling session', duration=60, difficulty='Intermediate'),
            Workout(_id=ObjectId(), name='Crossfit Challenge', description='High-intensity crossfit workout', duration=90, difficulty='Advanced'),
            Workout(_id=ObjectId(), name='Morning Run', description='5km morning run', duration=45, difficulty='Beginner'),
            Workout(_id=ObjectId(), name='Swimming Laps', description='Freestyle swimming laps', duration=30, difficulty='Intermediate'),
            Workout(_id=ObjectId(), name='Strength Circuit', description='Full-body strength training', duration=120, difficulty='Advanced'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
