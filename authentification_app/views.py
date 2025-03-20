from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UtilisateurSerializer, UtilisateurUpdateSerializer
from .models import Utilisateur
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def homepage(request):
    endpoints = {
        "Inscription": "http://127.0.0.1:8000/api/signup/",
        "Connexion": "http://127.0.0.1:8000/api/login/",
        "Liste des utilisateurs": "http://127.0.0.1:8000/api/utilisateurs/",
        "Modification des infos": "http://127.0.0.1:8000/api/user/update/"
    }
    return JsonResponse(endpoints)


@api_view(['GET'])
@permission_classes([AllowAny])
def list_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    serializer = UtilisateurSerializer(utilisateurs, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'GET':
        return Response({"message": "Veuillez envoyer une requête POST pour vous inscrire"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    if request.method == 'POST':
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def login_user(request):
    if request.method == 'GET':
        return Response({"message": "Veuillez envoyer une requête POST pour vous inscrire"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Veuillez fournir un email ou un mot de passe correcte'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=email, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Connexion réussie'}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Identifiants invalides'}, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['PUT', 'PATCH'])
@permission_classes([AllowAny])
def update_user_details(request, user_id):
    try:
        user = Utilisateur.objects.get(id=user_id)
        serializer = UtilisateurUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Utilisateur.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def logout_user(request):
    logout(request)
    return Response({'message': 'User logged out successfully'})