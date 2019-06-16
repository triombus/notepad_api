"""notepad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers

from event.views import EventViewSet
from note.views import NoteViewSet
from purchase.views import PurchaseViewSet, PurchaseItemViewSet

router = routers.DefaultRouter()
router.register(r'purchase', PurchaseViewSet, base_name='purchase')
router.register(r'purchaseitem', PurchaseItemViewSet, base_name='purchase-item')
router.register(r'event', EventViewSet, base_name='event')
router.register(r'note', NoteViewSet, base_name='note')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

