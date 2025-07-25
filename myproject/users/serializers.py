from rest_framework import serializers
from .models import User
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password','location']
    def create(self,validated_data):
        user=User.objects.create_user(
            user_name=validated_data['username'],
            password=validated_data['password'],
            location=validated_data['location']
        )
        return user