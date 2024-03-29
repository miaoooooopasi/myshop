# googd/views.py


from .models import Goods
from rest_framework import serializers
from .models import Goods,GoodsCategory


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"