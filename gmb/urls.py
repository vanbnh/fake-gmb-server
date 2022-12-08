
from django.urls import path

from gmb.views import get_account, get_list_account, get_local_post

urlpatterns = [
    path('accounts/', get_list_account, name='get_list_account'),
    path('<int:account_id>/', get_account, name='get_account'),

    path('accounts/<str:account_id>/locations/<str:location_id>/localPosts', get_local_post, name='get_local_post'),
]
