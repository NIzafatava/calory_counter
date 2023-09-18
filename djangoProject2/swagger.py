from django.urls import path, include
from drf_yasg.renderers import SwaggerUIRenderer
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework import response, schemas, permissions
from rest_framework.renderers import OpenAPIRenderer


# from rest_framework.sw.renderers import OpenAPIRenderer, SwaggerUIRenderer


schema_view = get_schema_view(
    info=openapi.Info(
        title='Api for calory app',
        default_version='v1',
        contact=openapi.Contact(name='nizafatava', email='izofatova.anastasia@yandex.ru'),
        license=openapi.License(name='License: Apache 2.0'),
    ),
    public=True,
    patterns=[
        path('', include('calory_counter.api.urls')),
    ],
    # authentication_classes=[
    #     BaseAuthentication,
    #     SessionAuthentication,
    #     TokenAuthentication,
    # ],
    # permission_classes=[IsAuthenticated,],
)