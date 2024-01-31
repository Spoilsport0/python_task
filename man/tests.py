from django.test import TestCase
from rest_framework import status
from .models import Person, Grade, Research
from rest_framework.test import APIClient
import json
from .forms import PersonRegistrationForm, GradeForm, ResearchForm
class PersonAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.person_data = {
            "first_name": "John",
            "second_name": "Doe",
            "age": 30,
            "login": "johndoe",
            "password": "password"
        }
        self.person = Person.objects.create(**self.person_data)

    def test_get_person_list(self):
        response = self.client.get('/api/person/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_person(self):
        new_person_data = {
            "first_name": "Alice",
            "second_name": "Smith",
            "age": 25,
            "login": "alicesmith",
            "password": "test456"
        }
        response = self.client.post('/api/person/create/', json.dumps(new_person_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_person_detail(self):
        response = self.client.get(f'/api/person/{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_person(self):
        updated_data = {
            "first_name": "Updated Name",
            "second_name": "Updated Surname",
            "age": 35,
            "login": "newlogin",
            "password": "newpassword"
        }
        response = self.client.put(f'/api/person/{self.person.id}/', json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_person(self):
        response = self.client.delete(f'/api/person/{self.person.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GradeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.grade_data = {
            "grade_of_research": 85,
            "grade_of_poster": 75,
            "grade_of_presentation": 90
        }
        self.grade = Grade.objects.create(**self.grade_data)

    def test_get_grade_list(self):
        response = self.client.get('/grade/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_grade(self):
        new_grade_data = {
            "grade_of_research": 70,
            "grade_of_poster": 80,
            "grade_of_presentation": 65
        }
        response = self.client.post('/grade/create/', json.dumps(new_grade_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_grade_detail(self):
        response = self.client.get(f'/grade/{self.grade.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_grade(self):
        updated_data = {
            "grade_of_research": 95,
            "grade_of_poster": 85,
            "grade_of_presentation": 92
        }
        response = self.client.put(f'/grade/{self.grade.id}/', json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_grade(self):
        response = self.client.delete(f'/grade/{self.grade.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ResearchAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person = Person.objects.create(
            first_name='John',
            second_name='Doe',
            age=30,
            login='johndoe',
            password='password'
        )
        self.grade = Grade.objects.create(
            grade_of_research=85,
            grade_of_poster=75,
            grade_of_presentation=90
        )
        self.research_data = {
            "title": "Research Title",
            "category": "Science",
            "person": self.person,
            "grade": self.grade
        }
        self.research = Research.objects.create(**self.research_data)

    def test_get_research_list(self):
        response = self.client.get('/research/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_research(self):
        new_research_data = {
            "title": "New Research",
            "category": "New Category",
            "person": self.person.id,
            "grade":self.grade.id
        }
        response = self.client.post('/research/create/', json.dumps(new_research_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_research_detail(self):
        response = self.client.get(f'/research/{self.research.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_research(self):
        updated_data = {
            "title": "Updated Research",
            "category": "Updated Category",
            "person": self.person.id,
            "grade": self.grade.id
        }
        response = self.client.put(f'/research/{self.research.id}/', json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_research(self):
        response = self.client.delete(f'/research/{self.research.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class RegisterPersonTestCase(TestCase):
    def test_register_person_creation(self):
        person_data = {
            "first_name": "John",
            "second_name": "Doe",
            "age": 30,
            "login": "johndoe",
            "password": "password"
        }
        form = PersonRegistrationForm(data=person_data)
        self.assertTrue(form.is_valid())
        new_person = form.save()
        self.assertEqual(new_person.first_name, 'John')

class CreateGradeTestCase(TestCase):
    def test_create_grade_valid_data(self):
        grade_data = {
            "grade_of_research": 85,
            "grade_of_poster": 75,
            "grade_of_presentation": 90
        }
        form = GradeForm(data=grade_data)
        self.assertTrue(form.is_valid())
        new_grade = form.save()
        self.assertEqual(new_grade.grade_of_research, 85)

class CreateResearchTestCase(TestCase):
    def test_create_research_valid_data(self):
        person = Person.objects.create(first_name='John', second_name='Doe', age=30, login="john", password="fk")
        grade = Grade.objects.create(grade_of_research=50, grade_of_poster=60, grade_of_presentation=70)

        research_data = {
            "title": "Sample Research",
            "category": "Science",
            "person": person.id,
            "grade": grade.id,
        }
        form = ResearchForm(data=research_data)
        self.assertTrue(form.is_valid())
        new_research = form.save()
        self.assertEqual(new_research.title, 'Sample Research')


