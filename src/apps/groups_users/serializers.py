from rest_framework import serializers
from .models import UserGroups


class GroupUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserGroups
        fields = ('pk', 'name', 'description')