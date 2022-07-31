
from django.urls import path
from .views import PlayerMertics_View

urlpatterns = [
   path('data', PlayerMertics_View.as_view())
]
