from django.shortcuts import render
from .models import Details
from django.http import HttpResponseRedirect

def form_view(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['phone']
        your_views = request.POST['yviews']
        callcheckbox = request.POST.get('callme', 'False')
        emailcheckbox = request.POST.get('emailme', 'False')
        
        new_query = Details( Name=fullname, email=email, phone=mobile, contact_via_phone=callcheckbox, contact_via_email=emailcheckbox, user_feedback = your_views )
        new_query.save()

    return render (request, 'baseapp/form.html')


def index_view(request):
    details = Details.objects.all()
    return render(request, "baseapp/index.html", context={ "details": details })