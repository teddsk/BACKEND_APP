from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UtilisateurSerializer, UtilisateurUpdateSerializer
from .models import Utilisateur
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.urls import reverse

@api_view(['GET'])
def homepage(request):
    endpoints = {
        "Inscription": "http://127.0.0.1:8000/api/signup/",
        "Connexion": "http://127.0.0.1:8000/api/login/",
        "Liste des utilisateurs": "http://127.0.0.1:8000/api/utilisateurs/",
        "Modification des infos": "http://127.0.0.1:8000/api/user/update/"
    }
    return JsonResponse(endpoints)


@api_view(['GET'])
def list_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    serializer = UtilisateurSerializer(utilisateurs, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
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
def login_user(request):
    if request.method == 'GET':
        return Response({"message": "Veuillez envoyer une requête POST pour vous inscrire"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'User logged in successfully'})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT', 'PATCH'])
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
def logout_user(request):
    logout(request)
    return Response({'message': 'User logged out successfully'})