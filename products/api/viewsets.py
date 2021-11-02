from products.api.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from products.models import Product


class ProductViewSet(GenericViewSet):

    def get_queryset(self, code=None):
        queryset = Product.objects.all()
        if code:
            queryset = Product.objects.filter(code=code)
        return queryset

    def create(self, request):
        print(request.data)
