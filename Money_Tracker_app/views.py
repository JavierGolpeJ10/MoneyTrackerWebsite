from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class Page(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class LoginPage(Page):

    def get(self, request):
        return render(request, "login_page.html")

    def post(self, request):
        return redirect("/home/")

    # def post(self, request):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #
    #     if username and password:
    #         return redirect("/home_page/")
    #     else:
    #         return render(request, "login_page.html",
    #                       {"message": "Username or Password is Incorrect!"})


class HomePage(Page):
    def get(self, request):
        return render(request, "home_page.html")