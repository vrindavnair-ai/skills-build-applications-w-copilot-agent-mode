from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "Thor", "age": 30},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "Tony", "age": 35},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "Steve", "age": 28},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]['_id'], users[1]['_id']]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[2]['_id']]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]['_id'], "activity_type": "Cycling", "duration": 60},
            {"_id": ObjectId(), "user": users[1]['_id'], "activity_type": "Running", "duration": 45},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]['_id'], "points": 100},
            {"_id": ObjectId(), "user": users[1]['_id'], "points": 90},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
