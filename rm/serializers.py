from rest_framework import serializers
from rm.models import recursivemenu
from rest_framework_recursive.fields import RecursiveField

class MenuSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    class Meta:
        model = recursivemenu
        fields = ('id', 'name', 'parent', 'children')


