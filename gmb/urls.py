
from django.urls import path

from gmb.views import get_account, get_list_account, get_location

urlpatterns = [
    path('accounts/', get_list_account, name='get_list_account'),
    path('<int:account_id>/', get_account, name='get_account'),
    path('locations/<int:location_id>/', get_location, name='get_list_location'),
]