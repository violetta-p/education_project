from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from education.models import Module
from education.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()


class ModuleListAPIView(generics.ListAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated]


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated]
