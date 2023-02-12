from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from home.models import Student
import re


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
            raise serializers.ValidationError("Email is not in correct format.")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Incorrect username or password.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
        )

        token, _ = Token.objects.get_or_create(user=user)

        return {
            'username': user.username,
            'token': token
        }

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    
    def validate(self, data):
        if not self.instance.check_password(data.get("old_password")):
            raise serializers.ValidationError("Incorrect old password.")
        
        if data.get("new_password") != data.get("confirm_password"):
            raise serializers.ValidationError("New password and confirm password fields do not match.")
        
        return data


class StudentSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = '__all__'

    def get_description(self, value):
        # return f'{value.first_name} {value.last_name} is a student at International Islamic University Islamabad.'
        return f'{value.first_name} {value.last_name} is a student at International Islamic University Islamabad. His student ID is {value.id}, and he is majoring in {value.major}. His current GPA is {value.gpa}'

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age must be a positive number")
        return value

    def validate_name(self, value):
        pattern = r'^[a-zA-Z]+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Name should only contain letters")
        return value

    def validate_major(self, value):
        # Check that the major is not empty
        if not value:
            raise serializers.ValidationError({'major': 'This field may not be blank.'})
        return value
    
    def validate_gpa(self, value):
        # Check that the gpa is within the range 0-4
        if value < 0 or value > 4:
            raise serializers.ValidationError({'gpa': 'GPA must be between 0 and 4.'})
        return value

