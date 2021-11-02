from rest_framework import routers
from rest_framework.routers import DefaultRouter
from products.api.viewsets import ProductViewSet


router = DefaultRouter()
router.register('products', ProductViewSet, basename='Product')

urlpatterns = router.urls
