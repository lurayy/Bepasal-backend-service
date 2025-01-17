from django.conf import settings as django_setting
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from users.api.auth import login, login_refresh, logout, whoami
from users.api.support_app import DocumentAPI, VerificationCodeAPI

router = SimpleRouter()
router.register('verifications', VerificationCodeAPI)

router.register('documents', DocumentAPI)

urlpatterns = [
    path('api/app/auth/refresh/', login_refresh),
    path('api/app/auth/logout/', logout),
    path('api/app/auth/', login),
    path('api/app/whoami/', whoami),
    path('api/users/', include('users.urls')),
    path('api/system/', include('system.urls')),
    path('api/site/', include('ecommerce.urls')),
]
urlpatterns += static(django_setting.MEDIA_URL,
                      document_root=django_setting.MEDIA_ROOT)
urlpatterns += static(django_setting.STATIC_URL,
                      document_root=django_setting.STATIC_ROOT)

SchemaView = get_schema_view(
    openapi.Info(
        title="BePasal API",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="himalayancreatives.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    urlconf='',
    patterns=[*urlpatterns],
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path("api/docs/",
         SchemaView.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui')
]

urlpatterns += [path('', admin.site.urls)]
