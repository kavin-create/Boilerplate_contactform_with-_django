from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method=='POST':
        print("helloo")
        name =request.POST.get('FullName')
        phonenumber =request.POST.get('PhoneNumber')
        email =request.POST.get('Email')
        message =request.POST.get('message')

        data={
            'name':name,
            'phonenumber':phonenumber,
            'email':email,
            'message':message,

        }
        print(data)
        message=("From {} /n".format('email')+data['message'])
        send_mail(data['phonenumber'],message,data['email'],['your emailid here'])
        

    return render(request, 'contact.html',{})