from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Pushups workout', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Running workout', difficulty='Medium'),
            Workout.objects.create(name='Deadlift', description='Deadlift workout', difficulty='Hard'),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='Pushups', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Running', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Deadlift', duration=60, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[3], score=95, rank=1)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
