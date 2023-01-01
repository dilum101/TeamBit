
from django.urls import path
from .views import Register,Login,getData
urlpatterns = [
   path('Register',Register, name="Register"),
   path('Login',Login, name="Login"),
   path('PlayerData',getData,name="playerData")
]
