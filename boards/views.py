from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
import requests
# Create your views here.
#print "shambhu first PYTHON app"
def home(request):
    boards = Board.objects.all()
    #return HttpResponse('Hello World!')
    print (" boards")
    print (boards)
    return render(request, 'home.html', {'boards': boards})

def checkSms(request):
    response = requests.get('https://2factor.in/API/V1/e55b6790-e5cf-11e9-9721-0200cd936042/BAL/SMS')
    sms_balance = response.json()
    return render(request, 'verify.html',{
        'status': sms_balance['Status'],
        'details': sms_balance['Details']
    })
def verify(request):
    #if 'mobile' in request.GET:
        mobile = request.GET['mobile']
    #if 'otp' in request.GET:
        otp = request.GET['otp']
        print('mobile number ',mobile)
        print('otp ',otp)
        url='http://2factor.in/API/V1/e55b6790-e5cf-11e9-9721-0200cd936042/SMS/%s/AUTOGEN' % mobile
        response = requests.get(url);
        sms_balance = response.json()
        print('response JSON ',sms_balance)
        return render(request, 'verify.html',{
            'status': sms_balance['Status'],
            'details': sms_balance['Details']
        })
