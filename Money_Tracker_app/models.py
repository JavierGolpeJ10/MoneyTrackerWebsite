from django.db import models

# Create your models here.

class MyUser(models.Model):

    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=50)
    # phone = models.CharField(max_length=50)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    # def get_email(self):
    #     return self.email
    #
    # def get_phone(self):
    #     return self.phone