import random
import string

from rest_framework import status, generics
from rest_framework.response import Response

from gmb.common.Accounts_reponse import Account, AccountList
from gmb.json_template.local_post import local_post_json_template
from gmb.models import Accounts

# Create your views here.
type_enum = ['ACCOUNT_TYPE_UNSPECIFIED', 'PERSONAL', 'LOCATION_GROUP', 'USER_GROUP', 'ORGANIZATION']
role_enum = ['ACCOUNT_ROLE_UNSPECIFIED', 'PRIMARY_OWNER', 'OWNER', 'MANAGER', 'SITE_MANAGER']
verdistate_enum = ['VERIFICATION_STATE_UNSPECIFIED', 'VERIFIED', 'UNVERIFIED', 'VERIFICATION_REQUESTED']
vettedstate_enum = ['VETTED_STATE_UNSPECIFIED', 'VETTED', 'NOT_VETTED', 'INVALID']
permissionlevel_enum = ['PERMISSION_LEVEL_UNSPECIFIED', 'OWNER_LEVEL', 'MEMBER_LEVEL']
"""
 {
      "name": "accounts/114963299403833404828",
      "accountName": "test",
      "type": "LOCATION_GROUP",
      "role": "PRIMARY_OWNER",
      "verificationState": "UNVERIFIED",
      "vettedState": "NOT_VETTED",
      "permissionLevel": "OWNER_LEVEL"
    }
"""
class GetAccount(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        account = self.kwargs['account_id']
        account_query = Accounts.objects.filter(name="accounts/"+str(account)).first()
        return Response(Account(self,account_query.id), status=status.HTTP_200_OK)
get_account = GetAccount.as_view()

class GetListAccount(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        account_query = Accounts.objects.all()
        if account_query is None:
            return Response({
                "message": "List account",
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(AccountList(self,account_query), status=status.HTTP_200_OK)

get_list_account = GetListAccount.as_view()


class GetLocalPost(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        post_ids = [''.join(random.choices(string.digits, k=16)) for _ in range(100)]
        data_list = [local_post_json_template(self.kwargs['account_id'], self.kwargs['location_id'], post_id)
                     for post_id in post_ids]
        data = {'location': data_list}
        return Response(data, status=status.HTTP_200_OK)


get_local_post = GetLocalPost.as_view()


