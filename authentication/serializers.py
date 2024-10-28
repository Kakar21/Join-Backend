from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for UserProfile model to include username, email, and color.
    """
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'color']

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email


class EmailAuthSerializer(serializers.Serializer):
    """
    Serializer for authenticating users with email and password.
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials.")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid login credentials.")

        data['user'] = user
        return data


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user with password confirmation and optional color.
    """
    repeated_password = serializers.CharField(write_only=True)
    color = serializers.CharField(
        write_only=True, allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'repeated_password', 'color']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        """
        Validates passwords, ensures email uniqueness, and creates User and UserProfile.
        """
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']

        if pw != repeated_pw:
            raise serializers.ValidationError(
                {'error': 'Ups! Your password don’t match'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'Ups! Your email already exist'})

        account = User(
            email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(pw)
        account.save()

        # Standardwert, falls color nicht übergeben wird
        color = self.validated_data.get('color', '#FFFFFF')
        UserProfile.objects.create(user=account, color=color)

        return account