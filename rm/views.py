from rest_framework.generics import ListAPIView

from .models import recursivemenu
from .serializers import MenuSerializer


class MenuList(ListAPIView):
    queryset = recursivemenu.objects.filter(parent__isnull=True)
    menus = recursivemenu.objects.all().order_by('-name', 'children__name')

    serializer_class = MenuSerializer
