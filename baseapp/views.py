from django.shortcuts import render
from .models import Details

def index_views(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['phone']
        checkbox1value = request.POST.get('checkbox1', 'False')
        if checkbox1value == 'True':
            sendvalue = "yes"

        print(fullname)
        print(sendvalue)
        new_query = Details(Name=fullname, email=email, phone=mobile,    if_selected=sendvalue )
        new_query.save()

    return render (request, 'baseapp/index.html')