from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.response import Response
from rest_framework import status


class MenuItemViewSet(viewsets.ViewSet):
    """
        CRUD Operations with View sets for Menu Item
    """
    permission_classes = [AllowAny]
    queryset = MenuItem.objects.all()

    def list(self, request):
        """
            Get all objects from menu item
        """
        srz_data = MenuItemSerializer(instance=self.queryset, many=True).data
        return Response(data=srz_data, status=status.HTTP_200_OK)

    def create(self, request):
        srz_data = MenuItemSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        menu_item = get_object_or_404(self.queryset, pk=pk)
        srz_data = MenuItemSerializer(instance=menu_item).data
        return Response(data=srz_data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        serializer = MenuItemSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        menu_item = get_object_or_404(self.queryset, pk=pk)
        srz_data = MenuItemSerializer(instance=menu_item, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_200_OK)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        menu_item = get_object_or_404(self.queryset, pk=pk)
        menu_item.delete()
        return Response({
            "Message": "Successfully menu item been deleted",
        })
