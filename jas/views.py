from django.http import JsonResponse

from serializers import PersonSerializer
from models import Person


def person_list(request):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    return JsonResponse(serializer.data, safe=False)
