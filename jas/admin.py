from django.contrib import admin
from jas.models import Person, Grade, Research

admin.site.register(Person)
admin.site.register(Research)
admin.site.register(Grade)