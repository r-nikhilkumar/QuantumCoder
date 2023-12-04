from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import user_contact_details
from django.contrib import messages
# Create your views here.
def index(request):
    inst = user_contact_details.objects.all()
    context = {
        "name1" : inst[0].name,
        "name2" : inst[1].name,
    }
            
    return render(request, "index.html",context)


def about(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        comment = request.POST.get('reason')
        contact = user_contact_details(name=name, phone = phone, email=email, comment= comment, date=datetime.today())
        contact.save()
        messages.success(request, "Contact Info sent Successfully!")
    return render(request, "about.html")


def moredetails(request):
    return render(request, "moreDetails.html")

def developer(request):
    return render(request, "developer.html")
def dashboard(request):
    return render(request, "dashboard.html")