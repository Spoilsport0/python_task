from django.db import models
import mysql.connector
from django.core.validators import MinValueValidator
from sqlalchemy.future import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
class Person(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=45)
    second_name = models.CharField(max_length=45)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    login = models.CharField(max_length=45, unique=False)
    password = models.CharField(max_length=45, unique=False)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

class Grade(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    grade_of_research = models.IntegerField()
    grade_of_poster = models.IntegerField()
    grade_of_presentation = models.IntegerField()

    def __str__(self):
        return f"Research: {self.grade_of_research}, Poster: {self.grade_of_poster}, Presentation: {self.grade_of_presentation}"

class Research(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='research')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='research_set', default=None)
    def __str__(self):
        return self.title



