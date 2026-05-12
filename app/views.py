from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST'])

def posts(request):
        if request.method == 'GET':
            return Response({'message': 'Welcome to the posts view!'}, status=status.HTTP_200_OK)
        if request.method == 'POST':
            return Response({'message': f'data is created by {request.user.username}'}, status=status.HTTP_200_OK)