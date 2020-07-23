from django.urls import path
from web.api.views import PersonListView, PersonCreateAPIView

urlpatterns = [
    path('person_list/', PersonListView.as_view(), name='person_list'),
    path('person_create/', PersonCreateAPIView.as_view(), name='person_create')
]
