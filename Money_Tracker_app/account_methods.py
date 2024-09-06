from Money_Tracker_app.models import *

class AccountInterface:

    def create_account(self, user_name, password, password1, permission, first_name, last_name):
        pass

    def get_accounts(self):
        pass

    def edit_account(self, email, phone, address, user):
        pass


class AccountMethods(AccountInterface):

    def create_account(self, user_name, password, password1, permission, first_name, last_name):
        try:
            username = MyUser.objects.get(user_name=user_name)

            if username is not None:
                return False
        except:
            if len(user_name) > 15 or len(first_name) > 15 or len(last_name) > 25 or len(password) > 15 or len(password1) > 15 or password != password1:
                return False

            new_account = MyUser(user_name=user_name, password=password,first_name=first_name, last_name=last_name)
            new_account.save()
            return True

        return False

    def get_accounts(self):
        try:
            accounts = MyUser.objects.all()
            return accounts
        except Exception as e:
            return False

    def edit_account(self, email, phone, address, user):
        user.set_