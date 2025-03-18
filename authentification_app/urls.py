from django.urls import path
from .views import signup, login_user, logout_user, update_user_details, list_utilisateurs, homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('api/signup/', signup, name='api_signup'),
    path('api/login/', login_user, name='api_login'),
    path('api/logout/', logout_user, name='api_logout'),
    path('api/user/update/', update_user_details, name='api_user_update'),
    path('api/utilisateurs/', list_utilisateurs, name='list_utilisateurs'),
]
