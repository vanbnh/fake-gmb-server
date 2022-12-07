import json

from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.response import Response
from gmb.common.Accounts_reponse import Account, AccountList

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
data_json_Location = "/Users/s19667/git/github/fake-gmb-server/location.json"
class GetAccount(generics.ListAPIView):
    # @ratelimit(key='ip', rate='10/m')
    def get(self, request, *args, **kwargs):
        account = self.kwargs['account_id']
        account_query = Accounts.objects.filter(name="accounts/"+str(account)).first()
        if account_query is None:
            return Response({
                "message": "Account not found",
            }, status=status.HTTP_404_NOT_FOUND)
        else:
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

class GetLocation( generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        location_id = self.kwargs['location_id']
        with open(data_json_Location) as json_file:
            data = json.load(json_file)
            if data['name'] == "locations/"+str(location_id):
                param = self.request.query_params.get('readMask', None)
                param = param.split(',')
                param = [x.strip() for x in param]
                f = open(data_json_Location)
                data = json.load(f)
                model_Location = get_query_param(request,data )
                list_column = [i for i in model_Location if i in param]
                header_param = get_name_query(self, data, list_column)
                with open('/Users/s19667/git/github/fake-gmb-server/lc.json', 'w') as f:
                    json.dump(header_param, f, indent=4,ensure_ascii=False )
                result = open('/Users/s19667/git/github/fake-gmb-server/lc.json')
                return HttpResponse(result, content_type='application/json')
            else:
                return Response({
                    "message": "Location not found",
                }, status=status.HTTP_404_NOT_FOUND)
get_location = GetLocation.as_view()

def get_name_query(self, data:dict, p: dict):
    local = {}
    for i in data:
        if i in p:
            local[i] = data[i]
    return local

def create_json(data: dict):
    local = {}
    for i in data:
        local[i] = data[i]
    return local
def get_query_param(request , data: dict):
    local = []
    for i in data:
        local.append(i)
    c =  create_json(data)
    return c

