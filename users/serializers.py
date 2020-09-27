from rest_framework import serializers
from users.models import Users


class UsersSerializers(serializers.Serializer):
    class Meta:
        model = Users
        fields = '__all__'
