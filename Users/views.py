from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import Token, RefreshToken

from Users.serializers import UserSerializer


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {'error': 'User does not exist.'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response(
                {'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token_refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'Login success',
            'username': user.username,
            'tokens': {
                'refresh': str(token_refresh),
                'access': str(token_refresh.access_token)}
            }, status=status.HTTP_200_OK)

class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'username': serializer.data['username'],
                    'message': 'User created successfully'
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
            refresh_token = request.data.get('refresh')

            if not refresh_token:
                return Response('Missing refresh token', status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'message': 'Logout success'}, status=status.HTTP_200_OK)
