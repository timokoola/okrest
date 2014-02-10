from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import link
from api.models import *
from api.serializers import *
from api.permissions import *


class HeadingViewSet(viewsets.ModelViewSet):

    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Heading.objects.all()
    serializer_class = HeadingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @link(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    """
    This endpoint presents the users in the system.

    As you can see, the collection of snippet instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
