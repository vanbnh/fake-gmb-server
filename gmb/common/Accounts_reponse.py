from typing import List, Dict, Any

from gmb.models import Accounts

def Account(self, account_id):
        self.account_id = account_id

        account_request = Accounts.objects.filter(id=account_id).first()
        return {
                "name": account_request.name,
                "accountName": account_request.accountName,
                "type": account_request.type,
                "role": account_request.role,
                "verificationState": account_request.verificationState,
                "vettedState": account_request.vettedState,
                "permissionLevel": account_request.permissionLevel,
            }


def AccountList(self, account_request):
    account= []
    for i in account_request:
        data = Account(self,i.id)
        account.append(data)
    return account
