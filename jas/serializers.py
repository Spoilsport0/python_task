from rest_framework import serializers
from jas.models import Person
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'second_name', 'age', 'login', 'password', 'grade']