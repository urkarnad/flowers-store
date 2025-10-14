from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_check = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)



    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_check']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Authomatic password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

    def validate(self, data):
        if data['password'] != data['password_check']:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def username_exists(self, username):
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError('Username already exists')

            if len(username) > 30:
                raise serializers.ValidationError('Username must be at most 30 characters')

            return username

    def email_validation(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')

        return email
