import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path


settings.configure(
    ALLOWED_HOSTS=["*"],
    ROOT_URLCONF=__name__,
)


urlpatterns = [
    path("", lambda request: HttpResponse("Hello World!")),
]


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
