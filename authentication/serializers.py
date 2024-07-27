from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
class SignUPViewSerializer(ModelSerializer):
    # first_name = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def create(self, validated_data):

        # This handles blank values if passed ie. last_name = ""
        if not validated_data.get('first_name'):
            raise serializers.ValidationError({'first_name': "This is a required field"})
        if not validated_data.get('last_name'):
            raise serializers.ValidationError({'last_name': "This is a required field"})

        # user = User.objects.create(**validated_data) #-- it would store the raw password as plain text, which is a significant security risk.
        # user = User.objects.create_user(**validated_data) # -- automatically hashes the password before saving it to the database.
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        # can be done this way too

        return user

    class Meta:
        model = User
        fields = ['id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email',
                  'is_staff', 'is_active', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},
            # it means that this field will only be used for write operations (e.g., POST requests) and will not be included in the serializer’s output (e.g., responses).
            'first_name': {'required': True},
            # ensures that these fields must be provided when creating or updating an instance through the serializer.
            'last_name': {'required': True}
            # This required checks if the whole key-value pair is present in api or not, if we have blank value(last_name = "") -> this will work fine. we need to handel it seperately in create method.
        }


class ResetPasswordViewSerializer(ModelSerializer):

    new_password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['new_password','email',]

