from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from system.api.products import (CategoryAPI, ProductAPI, ProductImageAPI,
                              ProductVariationAPI,
                              VariationOptionAPI, VariationTypeAPI)
from system.api.orders import OrderAPI, OrderItemStatusAPI, OrderStatusAPI

router = SimpleRouter()
router.register('categories', CategoryAPI)

router.register('products', ProductAPI)

router.register('status/order', OrderStatusAPI)
router.register('status/order-items', OrderItemStatusAPI)
router.register('orders', OrderAPI)

product_router = routers.NestedSimpleRouter(router,
                                            r'products',
                                            lookup='product')
product_router.register('images', ProductImageAPI)
product_router.register('variations', ProductVariationAPI)


router.register('variation-types', VariationTypeAPI)

variation_type_router = routers.NestedSimpleRouter(
    router, r'variation-types', lookup='variation_type')
variation_type_router.register('options', VariationOptionAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(variation_type_router.urls)),
]
