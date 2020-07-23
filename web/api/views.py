from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from web.api.serializers import PersonSerializer
from web.models import Person


class PersonListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonCreateAPIView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

