from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from calory_counter.api.serializers import (
    FoodSerializer,
    RecipeSerializer,
    ExerciseSerializer,
    ProfileSerializer,
)
from calory_counter.models import Food, Receipe, Exercise
from user.models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FoodListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Food.objects.all()
    lookup_url_kwarg = "food_id"
    lookup_field = "pk"
    serializer_class = FoodSerializer


class RecipeListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Receipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Receipe.objects.all()
    lookup_field = "pk"
    lookup_url_kwarg = "recipe_id"
    serializer_class = RecipeSerializer


class ExerciseListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Exercise.objects.all()
    lookup_field = "pk"
    lookup_url_kwarg = "exercise_id"
    serializer_class = ExerciseSerializer
