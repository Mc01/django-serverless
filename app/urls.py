from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.renderers import SwaggerJSONRenderer
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions


router = routers.DefaultRouter()


schema_view = get_schema_view(
   openapi.Info(
       title='Swagger API',
       default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny, ),
)


urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
    path('swagger.json', schema_view.as_cached_view(
        renderer_classes=(SwaggerJSONRenderer, ),
    )),
]
