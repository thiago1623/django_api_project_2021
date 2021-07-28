from rest_framework import serializers
from Models.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "name",
            "last_name",
            "email",
            "password",
            "profile_photo",
            "score_board",
            "created_at",
            "updated_at",
            "is_active",
            "is_superuser"
        )

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class UserTokenserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'name',
            'last_name',
            'email',
            'password',
            'score_board'
        )
