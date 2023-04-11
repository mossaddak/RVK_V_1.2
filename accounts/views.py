from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import  IsAuthenticated, AllowAny
from .serializers import  UserSerializer, UserGetSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.decorators import action
from .models import UserVerification
from rest_framework.views import APIView



#rest password
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


User = get_user_model()

class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    filterset_fields=["groups"]
    search_fields = ('phone_number', 'email')
    ordering_fields = ('email')
    ordering = ('-id')
    permission_classes = []
    parser_classes = [MultiPartParser]

   

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return UserSerializer
        else:
            return UserGetSerializer


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)


    def perform_update(self, serializer):
        if ('password' in self.request.data) and self.request.data['password']:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()


    @action(detail=False, methods=['POST'], name='verify_user', url_path="verify-user", parser_classes=[JSONParser])
    def verify_user(self, request):
        token = request.data.get('token', None)

        if token is not None:
            user_verification = UserVerification.objects.get(token=token)

            # check if link has already been used

            if user_verification.used == True:
                # send error
                return Response({"used": "Link has already been used"})
            else:
                user = user_verification.user
                user.verified = True
                user.is_active = True

                user.save()

                user_verification.used = True
                user_verification.save()

                return Response({"verified": True})
        else:
            return Response({"error": "Something went wrong!"})

    # @action(detail=False, methods=['POST'], name='forgot_password')
    # def forgot_password(self, request, *args, **kwargs):
    #     email = request.data['email']
    #     if User.objects.filter(email=email).exists():
    #         user = User.objects.get(email=email)
    #         send_email(email_type="password_reset", message='Your Password is reset', subject="Password Reset",
    #                    recipients=[email, ], username=user.username, uid=urlsafe_base64_encode(force_bytes(user.pk)),
    #                    token=account_activation_token.make_token(user))
    #         return JsonResponse(
    #             {'msg': 'We have sent you instructions on how to reset your password. Please check your mailbox.'})

    #     return Response({'msg': 'Incorrect email address. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)


    # @action(permission_classes=(IsAuthenticated,), detail=False, methods=['PATCH'], name='reset_password',
    #         serializer_class=PasswordSerializer)
    # def reset_password(self, request, *args, **kwargs):
    #     serializer = PasswordSerializer(data=request.data)

    #     if serializer.is_valid():
    #         if not request.user.check_password(serializer.data.get("old_password")):
    #             return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
    #         # set_password also hashes the password that the user will get
    #         request.user.set_password(serializer.data.get("new_password"))
    #         request.user.save()
    #         return Response("Success.", status=status.HTTP_200_OK)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=False, methods=['POST'], name='password_reset_confirm')
    # def password_reset_confirm(self, request, *args, **kwargs):
    #     uidb64 = request.data['uid']
    #     token = request.data['token']
    #     try:
    #         uid = force_str(urlsafe_base64_decode(uidb64))
    #         user = User.objects.get(pk=uid)
    #     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    #         user = None
    #     if user is not None and account_activation_token.check_token(user, token):
    #         user.set_password(request.data.get("password"))
    #         user.save()
    #         return JsonResponse({'msg': 'Password reset successfully'})
    #     else:
    #         return Response("User not exist or Invalid Link", status=status.HTTP_400_BAD_REQUEST)


# function to get current user in frontend
@swagger_auto_schema(operation_description="Get Current logged in user", methods=["get"], responses={200: UserGetSerializer(many=False)})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserGetSerializer(request.user, context={"request":request})
    return Response(serializer.data)


#forget password
# class PasswordResetRequestAPIView(APIView):
#     def post(self, request):
#         email = request.data.get('email')

#         print("email============================================",email)
        # user = User.objects.filter(email=email).first()
        # if user:
        #     token = default_token_generator.make_token(user)
        #     uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        #     reset_link = f"{request.build_absolute_uri('/')}/reset-password/{uidb64}/{token}/"

        #     message = render_to_string('password_reset_email.html', {'reset_link': reset_link})

        #     send_mail('Password Reset', message, 'noreply@yourdomain.com', [email], fail_silently=False)

        # return Response({'message': 'If this email address exists in our database, a password reset link has been sent to it.'})