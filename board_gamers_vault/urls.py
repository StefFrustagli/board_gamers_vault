"""board_gamers_vault URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500, handler403, handler405

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("marketplace/", include("marketplace.urls")),
    path("bag/", include("bag.urls")),
    path("checkout/", include("checkout.urls")),
    path("profiles/", include("profiles.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("", include("home.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Handling custom error pages
handler404 = "board_gamers_vault.views.handler404"
handler500 = "board_gamers_vault.views.handler500"
handler403 = "board_gamers_vault.views.handler403"
handler405 = "board_gamers_vault.views.handler405"
