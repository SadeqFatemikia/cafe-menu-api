from rest_framework import serializers

from .models import MenuItem, Category


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for Category model """

    class Meta:
        model = Category
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    """ Serializer for Menu Item model """
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = MenuItem
        fields = '__all__'
        read_only_fields = ('created_at',)
