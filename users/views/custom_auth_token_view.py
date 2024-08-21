from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from memento_django.settings import GOOGLE_CLIENT_ID, GOOGLE_DEVELOPER_KEY


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'google_client_id': GOOGLE_CLIENT_ID,
            'google_developer_key': GOOGLE_DEVELOPER_KEY
        })
