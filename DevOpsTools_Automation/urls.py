from django.contrib import admin
from django.urls import path, include
from GHE_User_Billing_Website import views
from DVT_api.views import login
from DVT_api.views import get_user
from DVT_api.views import post_user



urlpatterns = [
    #path('home/', views.home),
    path('admin/', admin.site.urls),
    path('api/', include('DVT_api.urls')),
    path('', include('GHE_User_Billing_Website.urls')),
    path('api/login', login),
    path('api/get_user', get_user),
    path('api/post_user', post_user),
]

#Configure Admin Titles 

admin.site.site_header = "PwC - Github Enterprise - User Billing Administration"
admin.site.site_title = "PwC_GHE-User_Billing"
admin.site.index_title = " "

