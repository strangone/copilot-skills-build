from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password')
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30)
        self.assertEqual(activity.activity_type, 'Running')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Description', duration=60)
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.duration, 60)
