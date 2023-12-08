from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
