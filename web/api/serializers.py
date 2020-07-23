from rest_framework import serializers

from web.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'






# class JobOffersListView(ListAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = JobSerializers
#     queryset = JobOffers.objects.all()


    # path('job_list/', JobOffersListView.as_view(), name='job_list'),
