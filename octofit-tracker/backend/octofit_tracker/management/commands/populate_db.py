from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@kent.com', password='superman', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        Activity.objects.create(user=clark, type='run', duration=50, distance=10)

        # Create Workouts
        Workout.objects.create(name='Avengers HIIT', description='High intensity workout for Marvel heroes')
        Workout.objects.create(name='Justice League Strength', description='Strength workout for DC heroes')

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=90)
        Leaderboard.objects.create(user=bruce, points=95)
        Leaderboard.objects.create(user=clark, points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
