from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request, 'contact.html')

def worthy(request):
    if request.user.is_anonymous:
        return HttpResponse("BAKA")
    req={"name": Contact.objects.last().name,
         "email": Contact.objects.last().email,
         "phone": Contact.objects.last().phone,
         "desc": Contact.objects.last().desc,
         "date": Contact.objects.last().date}
    req=json.dumps({k:str(v) for (k,v) in req.items()})
    return HttpResponse(req)
    # return HttpResponse("WELCOME SHADOW")
