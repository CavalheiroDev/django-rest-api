from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from products.api.serializers import ProductSerializer
from products.models import Product


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        queryset = Product.objects.all()
        if pk:
            queryset = Product.objects.filter(code=pk)
        return queryset

    def create(self, request):
        product = request.data

        serializer = self.serializer_class(data=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
