from Money_Tracker_app.models import *

class ValidationInterface:

    def validate_login(self, username, password):
        pass


class Validation(ValidationInterface):

    def validate_login(self, username, password):
        no_user = False
        bad_password = False

        try:
            user = MyUser.objects.get(username=username)
            bad_password = (user.password != password)
        except:
            no_user = True

        if no_user or bad_password:
            return False
        else:
            return True