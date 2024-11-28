"""
URL configuration for giftcard_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

"""
Note django.contrib.auth.urls includes:
* accounts/login/ [name="login"]
* accounts/logout/ [name="logout"]
* accounts/password_change/ [name="password_change"]
* accounts/password_change/done/ [name="password_change_done"]
* accounts/password_reset/ [name="password_reset"]
* accounts/password_reset/done/ [name="password_reset_done"]
* accounts/reset/<uidb64>/<token>/ [name="password_reset_confirm"]
* accounts/reset/done/ [name="password_reset_complete"]
"""

urlpatterns = [
    # Django admin:
    path('admin/', admin.site.urls),

    # User management:
    path('accounts/', include('django.contrib.auth.urls')),

    # Local apps - believe need to order from most to least specific:
    path('accounts/', include('accounts.urls')),
    path('giftcards/', include('giftcards.urls')),
    path('shop/', include('shop.urls')),
    path('faq/', include('faq.urls')),
    path('', include('main.urls')),
]
