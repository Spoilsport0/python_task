"""man URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from man import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/person/', views.person_list, name="user_list"),
    path('api/person/<int:person_id>/', views.user_detail, name='user_detail'),
    path('api/person/create/', views.create_user, name='create_user'),
    path('grade/', views.grade_list, name="grade_list"),
    path('grade/<int:grade_id>/', views.grade_detail, name='grade_detail'),
    path('grade/create/', views.create_grade, name='create_grade'),
    path('research/', views.research_list, name="research_list"),
    path('research/<int:research_id>/', views.research_detail, name='research_detail'),
    path('research/create/', views.create_research, name='create_research'),
    path('all_students_rating/', views.all_students_rating, name='all_students_rating'),
    path('register/', views.register_person, name='register_person'),
    path('create_grade/', views.create_grade, name='create_grade'),
    path('create_research/', views.create_research, name='create_research'),
]

urlpatterns = format_suffix_patterns(urlpatterns)