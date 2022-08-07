"""sumuma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    path('x9T5y2sg/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('kakeibo/', include('kakeibo.urls')),
    path('analyses/', include('analyses.urls')),
    path('contact/', include('contact.urls')),
    path('budget/', include('budget.urls')),
    path('shopping/', include('shopping.urls')),
    path('lp/', include('lp.urls')),
]
