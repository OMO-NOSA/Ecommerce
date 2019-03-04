from django.urls import path
from accounts.views import(
                            register,
                            login,
                            logout
                            )

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register',register, name='register'),
]

