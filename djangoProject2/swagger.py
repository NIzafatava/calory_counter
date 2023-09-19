from django.urls import path, include
from drf_yasg import openapi

# from drf_yasg.renderers import SwaggerUIRenderer
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    info=openapi.Info(
        title="Api for calory app",
        default_version="v1",
        contact=openapi.Contact(
            name="nizafatava", email="izofatova.anastasia@yandex.ru"
        ),
        license=openapi.License(name="License: Apache 2.0"),
    ),
    public=True,
    patterns=[
        path("", include("calory_counter.api.urls")),
    ],
    # authentication_classes=[
    #     BaseAuthentication,
    #     SessionAuthentication,
    #     TokenAuthentication,
    # ],
    # permission_classes=[IsAuthenticated,],
)
