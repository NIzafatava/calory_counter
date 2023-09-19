from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from calory_counter.api.views import (
    FoodListCreateApiView,
    RecipeListCreateApiView,
    ExerciseListCreateApiView,
    FoodDeleteUpdateApiView,
    ExerciseDeleteUpdateApiView,
    RecipeDeleteUpdateApiView,
    ProfileViewSet,
)

router = routers.DefaultRouter()
router.register(r"apiprofile", ProfileViewSet)


urlpatterns = [
    path("api/v1/foodlist/", FoodListCreateApiView.as_view()),
    path("api/v1/foodlist/<int:food_id>/", FoodDeleteUpdateApiView.as_view()),
    path("api/v1/recipelist/", RecipeListCreateApiView.as_view()),
    path("api/v1/recipelist/<int:recipe_id>/", RecipeDeleteUpdateApiView.as_view()),
    path("api/v1/exerciselist/", ExerciseListCreateApiView.as_view()),
    path(
        "api/v1/exerciselist/<int:exercise_id>/", ExerciseDeleteUpdateApiView.as_view()
    ),
    path("", include(router.urls)),
    path("api/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/auth/", include("djoser.urls.authtoken")),
]
