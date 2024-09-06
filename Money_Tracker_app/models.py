from django.db import models

# Create your models here.

class MyUser(models.Model):

    user_name = models.CharField(max_length=15)
    user_password = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    # email = models.CharField(max_length=50)
    # phone = models.CharField(max_length=50)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name
        self.save()

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name
        self.save()

    # def get_email(self):
    #     return self.email
    #
    # def get_phone(self):
    #     return self.phone