from django.urls import path
from GHE_User_Billing_Website import views

urlpatterns = [
    path('home/', views.home),
    path('users/', views.all_users, name="list-users"),
    path('add_users_manually/', views.add_users_manually, name = "add-users-manually"),
    path('show_user/<user_id>', views.show_user, name='show-user'),
    path('update_user/<user_id>', views.update_user, name='update-user'),
    path('search_user/', views.search_user, name= 'search-user'),
]