from django.utils import timezone

from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from ..models import Event
from ..serializers import EventSerializer


class EventView(generics.ListCreateAPIView):
    DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
    authentication_classes = [TokenAuthentication]
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        start_date_str = self.request.GET.get('from')
        end_date_str = self.request.GET.get('to')

        start_date = timezone.datetime.strptime(start_date_str, self.DATE_TIME_FORMAT)
        end_date = timezone.datetime.strptime(end_date_str, self.DATE_TIME_FORMAT)
        breakpoint()
        queryset = Event.objects.filter(entry__user=self.request.user).filter(starts_at__range=(start_date, end_date))

        return queryset.order_by('starts_at')
