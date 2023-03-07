"""MY_SHOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from .api.store import StoreView
from .api.customer import CustomerView
from .api.item_category import ItemCategoryView
from .api.item import ItemView
from .api.mybag import MyBugView
from .api.purchase import PurchaseView
from .api.store_category import StoreCategoryView
from .api.store_owner import StoreOwnerView
from MY_SHOP.polls.views import LoginView, RegisterView, LogoutView, verify_email, MyTokenObtainPairView, MyTokenRefreshView


#_______________________________________________________________________________


urlpatterns = [
    path("store/", StoreView.as_view()),
    path("customer/", CustomerView.as_view()),
    path("item_category/", ItemCategoryView.as_view()),
    path("item/", ItemView.as_view()),
    path("myBag/", MyBugView.as_view()),
    path("purchase/", PurchaseView.as_view()),
    path("store_category/", StoreCategoryView.as_view()),
    path("store_owner/", StoreOwnerView.as_view()),
    path('admin/', admin.site.urls),
    path('polls/', include('MY_SHOP.polls.urls')),
    path('api/login/', LoginView.as_view()),
    path('api/register/', RegisterView.as_view()),
    path('api/logout/', LogoutView.as_view()),
    path('verify-email/', verify_email, name='verify_email'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),

]


#_______________________________________________________________________________


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)



