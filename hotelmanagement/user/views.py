from django.shortcuts import render
from hotel.models import hoteldetails
from django.contrib.auth.models import User


# Create your views here.
def test(request):
    return render(request,'usert/test.html')


def userviewhotel(request):
    hotels = hoteldetails.objects.all()
    return render(request, 'usert/userviewhotel.html', {'hotels': hotels})


def userhome(request):
    return render(request, 'usert/userhome.html')


def userviewprofile(request):
    return render(request, 'usert/userviewprofile.html',)


def useraddemail(request):
    if request.method == "POST":
        email = request.POST.get('emailu')
        cuser = request.user
        cuser.email=email
        cuser.save()
        return render(request,'usert/userviewprofile.html')


def useraddfirstname(request):
    if request.method == "POST":
        email = request.POST.get('firstnameu')
        cuser = request.user
        print(cuser.email)
        cuser.first_name=email
        cuser.save()
        return render(request,'usert/userviewprofile.html')


def useraddlastname(request):
    if request.method == "POST":
        email = request.POST.get('lastnameu')
        cuser = request.user
        print(cuser.email)
        cuser.last_name=email
        cuser.save()
        return render(request,'usert/userviewprofile.html')