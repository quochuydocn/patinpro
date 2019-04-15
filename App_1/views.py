from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ListGiay
from django.utils import timezone
import requests

# Create your views here.

def github(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'core/github.html', {'search_result': search_result})

def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

def home1(request):
    return redirect("accounts/login/")


def Control(request):
    listGiay = ListGiay.objects.all()
    return render(request, 'TabElement/Control.html', { 'listGiay': listGiay })


def Detail(request, shoe_pk):
    shoe = ListGiay.objects.get(pk=shoe_pk)
    listGiay = ListGiay.objects.all()
    gia = 25000/60
    success = 0
    summ = None
    layoutTien = 0
    tien = 0

    if request.method == 'POST':
        if shoe.Borrow == 0:
            shoe.Borrow = 1
            shoe.BorrowTimes = shoe.BorrowTimes + 1
            shoe.TimeBorrow = timezone.localtime()
            shoe.TimeReturn = None
            shoe.save()
            success = 1
        else:
            shoe.Borrow = 0
            shoe.TimeReturn = timezone.localtime()
            shoe.save()
            summ = (shoe.TimeReturn.day*24*60 + shoe.TimeReturn.hour*60 + shoe.TimeReturn.minute) - (shoe.TimeBorrow.day*24*60 + shoe.TimeBorrow.hour*60 + shoe.TimeBorrow.minute)
            summ = shoe.TimeReturn - shoe.TimeBorrow
            tien = summ.seconds*8.5
            layoutTien = str(int(tien//1000)) + "," + str(int(tien - int(tien//1000)*1000)) + ".00"
            #tien = summ*gia
            success = 1
        # return render(request, 'TabElement/Detail.html', { 'shoe': shoe })

        return render(request, 'TabElement/Detail.html', { 'shoe': shoe, 'success': success, 'summ': layoutTien, 'phut': summ })
    return render(request, 'TabElement/Detail.html', { 'shoe': shoe, 'success': success, 'summ': layoutTien, 'phut': summ })
