from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.permissions import IsModerator, IsOwner
from habits.serializers import HabitsSerializer


class HabitCreate(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, ~IsModerator, ]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class HabitList(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsOwner | IsModerator, ]


class HabitRetrieve(generics.RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsOwner | IsModerator, ]


class HabitUpdate(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsOwner | IsModerator, ]

    def perform_update(self, serializer):
        update_lesson = serializer.save()
        update_lesson.owner = self.request.user
        update_lesson.save()


class HabitDelete(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = [IsOwner, ~IsModerator]
