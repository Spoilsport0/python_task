from django import forms
from .models import Person, Research, Grade

class PersonRegistrationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'second_name', 'age', 'login', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = ('title', 'category', 'person', 'grade')

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('grade_of_research', 'grade_of_poster', 'grade_of_presentation')