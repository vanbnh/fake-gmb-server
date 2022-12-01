
from django.urls import path

from gmb.views import create_account, get_account, get_list_account

urlpatterns = [
    path('accounts/', get_list_account, name='get_list_account'),
    path('<int:account_id>/', get_account, name='get_account'),
]