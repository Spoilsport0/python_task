from rest_framework import serializers
from .models import Person, Research, Grade
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'grade_of_research', 'grade_of_poster', 'grade_of_presentation']
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'second_name', 'age', 'login', 'password']

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ['id', 'title', 'category', 'person', 'grade']




