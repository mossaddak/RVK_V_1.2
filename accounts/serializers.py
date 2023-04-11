from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import Group
from events.models import Event

from payment_methodology.serializer import(
    DonationSerializer
)


User = get_user_model()




# custom serializer to allow user log in
class CustomJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'email': '',
            'password': attrs.get("password")
        }
        User = get_user_model()
        
        # get user using email or phone number
        user_obj = User.objects.filter(email=attrs.get("email")).first() or User.objects.filter(
            phone_number=attrs.get("email")).first()

        if user_obj:
            credentials['email'] = user_obj.email

            if user_obj.is_superuser:
                return super().validate(credentials)

            elif user_obj.verified:
                # only allow verified users to log in
                return super().validate(credentials)
            else:
                raise PermissionDenied("This user need to verify")

        return super().validate(credentials)



class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('codename',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "__all__"
            )

        extra_kwargs = {
            'password': {'write_only': True},
        }


class EventSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'
    
    def get_created_at(self, obj):

        # Get the datetime object
        created_at = obj.created_at
        
        formatted_date = created_at.strftime("%Y-%m-%d")

        return formatted_date



class UserGetSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()
    dob = serializers.SerializerMethodField()

    Donation = DonationSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        exclude=("password","verified",)
    
    def get_profile_picture(self, obj):
        if obj.profile_picture:
            return self.context['request'].build_absolute_uri(obj.profile_picture.url)
        else:
            return None
    
    def get_dob(self, obj):

        # Get the datetime object
        dob = obj.dob

        if dob:
            formatted_date = dob.strftime("%Y-%m-%d")

            return formatted_date
        else:
            return ""
    

    # def get_events(self, obj):
    #     events = Event.objects.filter(registrants=obj)

    #     serializer = EventSerializer(events, many=True)

    #     return serializer.data