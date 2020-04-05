from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username

    @classmethod
    def generate(cls):
        import requests
        u = requests.get('https://randomuser.me/api/?nat=us').json()['results'][0]
        return cls.objects.create(
            username=u['login']['username'],
            email=u['email'],
            first_name=u['name']['first'],
            last_name=u['name']['last'],
        )
