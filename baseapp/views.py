from django.shortcuts import render
from .models import addDetails

def index_views(request):
    if request.method == 'POST':
        fullname = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['phone']
        yviews = request.POST['ybiews']


        new_query = addDetails(Name=fullname, email=email, phone=mobile, yviews=yviews )
        new_query.save()

    return render (request, 'baseapp/index.html')