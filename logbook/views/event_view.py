from django.utils import timezone
from django.utils.dateparse import parse_datetime

from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from ..models import Event
from ..serializers import EventSerializer


class EventView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        start_date_str = self.request.GET.get('from')
        end_date_str = self.request.GET.get('to')

        start_date = parse_datetime(start_date_str)
        end_date = parse_datetime(end_date_str)

        queryset = Event.objects.filter(entry__user=self.request.user).filter(starts_at__range=(start_date, end_date))

        return queryset.order_by('starts_at')
