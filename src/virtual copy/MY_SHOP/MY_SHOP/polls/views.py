
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .email import send_verification_email
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView
from MY_SHOP.polls.serializers import MyTokenObtainPairSerializer


#_______________________________________________________________________________

class LoginView(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=400)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk})


#_______________________________________________________________________________


class RegisterView(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not username or not email or not password:
            return Response({'error': 'Please provide all required fields'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)
        
        hashed_password = make_password(password)
        user = User.objects.create(username=username, email=email, password=hashed_password)
        token, created = Token.objects.get_or_create(user=user)

        user = User.objects.create_user(username=username, email=email, password=password)
        send_verification_email(user)

        return Response({'token': token.key, 'user_id': user.pk})
#_______________________________________________________________________________


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'success': 'Logged out successfully'})

#_______________________________________________________________________________

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_email(request):
    data = request.data
    user_id = request.user.id
    
    try:
        user = User.objects.get(id=user_id)
        if user.email_verified:
            return Response({'message': 'Email address has already been verified.'})
        
        if user.verification_code == data['verification_code']:
            user.email_verified = True
            user.save()
            return Response({'message': 'Email address has been successfully verified.'})
        else:
            return Response({'message': 'Verification code is invalid.'})
    except ObjectDoesNotExist:
        return Response({'message': 'User does not exist.'})
    
#_______________________________________________________________________________

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            refresh_token = response.data['refresh']
            access_token = response.data['access']
            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True, samesite='None', secure=True)
            response.data = {'access_token': access_token}
        return response

#_______________________________________________________________________________


class MyTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            refresh_token = response.data['refresh']
            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True, samesite='None', secure=True)
        return response
