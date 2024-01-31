from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer, GradeSerializer, ResearchSerializer
from .models import Person, Grade, Research
from rest_framework.decorators import api_view
from django.db.models import F, Sum
from django.shortcuts import render, redirect
from .forms import PersonRegistrationForm, ResearchForm, GradeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
@api_view(['GET', 'POST'])
def person_list(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return JsonResponse({"persons":serializer.data})
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, person_id):
    try:
        user = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PersonSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = PersonSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = PersonSerializer(user)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def grade_list(request, format=None):
    if request.method == 'GET':
        grade = Grade.objects.all()
        serializer = GradeSerializer(grade, many=True)
        return JsonResponse({"grade":serializer.data})
    if request.method == 'POST':
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def grade_detail(request, grade_id):
    try:
        grade = Grade.objects.get(pk=grade_id)
    except Grade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GradeSerializer(grade)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        grade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = GradeSerializer(grade)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def create_grade(request):
    serializer = GradeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def research_list(request):
    if request.method == 'GET':
        research = Research.objects.all()
        serializer = ResearchSerializer(research, many=True)
        return JsonResponse({"research":serializer.data})
    if request.method == 'POST':
        serializer = ResearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def research_detail(request, research_id):
    try:
        research = Research.objects.get(pk=research_id)
    except Research.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ResearchSerializer(research)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = ResearchSerializer(research, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        research.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = ResearchSerializer(research)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def create_research(request):
    serializer = ResearchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def person_list_sorted_by_grade(request):
    persons_sorted = Person.objects.order_by('-grades__grade_value').distinct()
    serializer = PersonSerializer(persons_sorted, many=True)
    return JsonResponse({"persons_sorted_by_grade": serializer.data})

@api_view(['GET'])
def all_students_rating(request):
    students_with_rating = (
        Person.objects.annotate(
            total_grade=Sum(
                F('research__grade__grade_of_research') +
                F('research__grade__grade_of_poster') +
                F('research__grade__grade_of_presentation')
            )
        )
        .order_by('-total_grade')
    )

    serializer = PersonSerializer(students_with_rating, many=True)
    return Response(serializer.data)


def register_person(request):
    if request.method == 'POST':
        form = PersonRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('create_grade'))
    else:
        form = PersonRegistrationForm()

    return render(request, 'register_person.html', {'form': form})

def create_research(request):
    if request.method == 'POST':
        form = ResearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_students_rating')
    else:
        form = ResearchForm()
    return render(request, 'create_research.html', {'form': form})

def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_research')
    else:
        form = GradeForm()

    return render(request, 'create_grade.html', {'form': form})


