from django.shortcuts import render,redirect
from .models import UserComment




def feed(request):
    if request.method =='GET':
        data=reversed(UserComment.objects.all())
        return render(request, 'feed.html',{'data':data})
    else:
        UserComment(
        commment=request.POST['com']
        ).save()
        data=reversed(UserComment.objects.all())
        return render(request, 'feed.html',{'data':data})

