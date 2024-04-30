from django.shortcuts import render, redirect
from .forms import hoteldetailsform, hotelstaffmanagement
from .models import hoteldetails, staffmanagement
from django.contrib.auth.models import User

# Create your views here.
def hotelhome(request):
    return render(request,'hotelt/hotelhome.html')


def uploadhotel(request):
    if request.method == 'POST':
        form = hoteldetailsform(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('viewhotel')
    else:
        form = hoteldetailsform()

    return render(request, 'hotelt/uploadhotel.html', {'form': form})


def viewhotel(request):
    hotels = hoteldetails.objects.all()
    return render(request, 'hotelt/viewhotel.html',{'hotels': hotels})


def hotelviewprofile(request):
    return render(request, 'hotelt/hotelviewprofile.html',)


def hoteladdemail(request):
    if request.method == "POST":
        email = request.POST.get('emailu')
        cuser = request.user
        cuser.email=email
        cuser.save()
        return render(request,'hotelt/hotelviewprofile.html')


def hoteladdfirstname(request):
    if request.method == "POST":
        email = request.POST.get('firstnameu')
        cuser = request.user
        print(cuser.email)
        cuser.first_name=email
        cuser.save()
        return render(request,'hotelt/hotelviewprofile.html')


def hoteladdlastname(request):
    if request.method == "POST":
        email = request.POST.get('lastnameu')
        cuser = request.user
        print(cuser.email)
        cuser.last_name=email
        cuser.save()
        return render(request,'hotelt/hotelviewprofile.html')


def hotelstaffmanagementht(request):
    staff = staffmanagement.objects.all()
    return render(request, 'hotelt/hotelstaffmanagement.html',{'staff': staff})


def hoteladdstaff(request):
    if request.method == 'POST':
        form = hotelstaffmanagement(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('hotelstaffmanagementht')
    else:
        form = hotelstaffmanagement()
    return render(request, 'hotelt/hoteladdstaff.html', {'form': form})