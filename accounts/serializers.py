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

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


#User = get_user_model()

from .models import User
from rest_framework.response import Response



# custom serializer to allow user log in
class CustomJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'email': '',
            'password': attrs.get("password")
        }
        User = User
        
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
    Donation = DonationSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            "password",
            "name",
            "email",
            "smart_card",
            "gender",
            "age",
            "address",
            "city",
            "state",
            "profile_picture",
            "country",
            "Donation",
            "phone_number",
            "country"
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        request = self.context.get('request')
        current_user_id = request.user.id if request and request.user else None
        if User.objects.filter(email = data['email']).exclude(id=current_user_id).exists():
            raise serializers.ValidationError("user already exist")
        return data
    
    def create(self, validate_data):
        user = User.objects.create(
            
            # email=validate_data["email"],
            # phone_number = validate_data["phone_number"],
            # name=validate_data["name"],
            # smart_card=validate_data["smart_card"],
            # gender=validate_data["gender"],
            # age=validate_data["age"],
            # address=validate_data["address"],
            # city=validate_data["city"],
            # state=validate_data["state"],
            # profile_picture=validate_data["profile_picture"],
            # country=validate_data["country"],

            email=validate_data.get("email", "none"),
            phone_number=validate_data.get("phone_number", "none"),
            name=validate_data.get("name", "none"),
            # smart_card=validate_data.get("smart_card", "none"),
            # gender=validate_data.get("gender", "none"),
            # age=validate_data.get("age", "none"),
            # address=validate_data.get("address", "none"),
            # city=validate_data.get("city", "none"),
            # state=validate_data.get("state", "none"),
            # profile_picture=validate_data.get("profile_picture", "none"),
            # country=validate_data.get("country", "none"),

        )
        print("End User======================", user)
        user.set_password(validate_data["password"])
        user.save()

        return validate_data
    




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
    #profile_picture = serializers.SerializerMethodField()
    #dob = serializers.SerializerMethodField()

    #Donation = DonationSerializer(many=True, read_only=True)
    
    class Meta:
        #model = get_user_model()
        model = User
        fields = (
            'id',
            # 'name',
            # "email",
            # "smart_card",
            # "gender",
            # "age",
            # "address",
            # "city",
            # "state",
            # "profile_picture",
            # "country",
            # "verified",
            #"Donation",
        )
        #exclude=("password","verified",)

    
    
    
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



class VeriFyAccountSerializer(serializers.Serializer):
    #email = serializers.EmailField()
    otp = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    

    def validate(self, data):

        print("data================================================", data)
        email = data['email']
        if not User.objects.filter(email = email).exists():
             raise serializers.ValidationError("Account not found")
        user = User.objects.filter(email=email)
        user = user[0]
        user.verified
        
        if user.verified == False:
            raise serializers.ValidationError("Account is not verified")
        print("NEwemial=================================", user.verified)
        return data
    
    
    def get_jwt_token(self, data):

        user = authenticate(email=data['email'], password=data['password'])
        print("user===========================================", user)


        

        if not user:
            return {
                'message':'invalid credentials',
                'data':{}
            }
        
        
        
        refresh = RefreshToken.for_user(user)
        return { 
                'message':'Login Success',
                'data':{
                    'token':{
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }

                }
            }