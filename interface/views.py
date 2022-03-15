from django.shortcuts import render, redirect

from django.urls import reverse

from django.utils import timezone

from datetime import datetime

def interface_view(request):

    myDate = datetime.now()

    return render(request, 'interface/index.html', {
        'myDate': myDate,
        'opacity1': 1,
        'opacity2': 1,
        'opacity3': 1,
    })
