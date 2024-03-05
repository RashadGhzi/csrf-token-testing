from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt
# Create your views here.


@api_view(['POST'])
@csrf_protect
def ProductView(request):
    # print the csrf token
    # print(request.COOKIES.get('csrftoken'))
    if request.method == 'POST':
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'product.html', context=None)


@api_view(['GET'])
@ensure_csrf_cookie
def csrf_cookie(request):
    return Response({'message': 'CSRF cookie set'})
