from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.messages import error
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .models import *
  # the index function is called when root is visited
# Create your views here.
# urlpatterns = [
#     url(r'^$', views.index),     # This line has changed!
#     url(r'^(?P[0-9]{2})$', views.show),
#     url(r'^(?P[0-9]{2})/edit$', views.edit),
#     url(r'^/new$', views.new),
#     url(r'^/create$', views.create),
#     url(r'^/<id>/delete$',views.delete),
#     url(r'^/<id>$',views.update, name='my_update')
# ]
def index(request):
    # context = {
    #     "userList": User.objects.all()
    #     }
    userList = User.objects.all() 
    print userList
    print "inside index" 
    #Doing the datetime formatting to convert in expected format 
    for user in userList:
        user.created_at = (user.created_at).strftime('%B %d, %Y')
    for user in userList:
        print "user.first_name:",user.first_name
        print "user.last_name:",user.last_name
        print "user.email:", user.email
        # print "user.created_at", user.created_at.date()
        print "user.created_at",(user.created_at)
        context = {
        "users": userList
        }
    return render(request,'UserDetails/index.html', context)

def new(request):
    return render(request, 'UserDetails/new.html')


def create(request):
    result = User.objects.register_validator(request.POST)
    if type(result) == list and len(result)>0:
        for error in result:
            messages.error(request, error)
        return redirect('/new')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully created user!")
    return redirect('/')

def show(request, id):
    user_id = id
    print "Inside Show method"
    print user_id
    userObj = User.objects.get(id = user_id)
    userObj.created_at = (userObj.created_at).strftime('%B %d, %Y')
    context={
        "user": userObj
    }
    return render(request, 'UserDetails/show.html', context )

def edit(request, id):
    id = id
    userObj = User.objects.get(id = id)
    print "edit"
    context = {
        'id' : id,
        'user': userObj
    }
    
    return render(request, 'UserDetails/edit.html', context )


def delete(request,id):
    dest = User.objects.get(id = id)
    dest.delete()
    return redirect('/')

def update (request,id):
    id = id
    result = User.objects.register_validator(request.POST)
    if type(result) == list and len(result)>0:
        for error in result:
            messages.error(request, error)
        return redirect('/{}/edit'.format(id))
    print id
    # instead of a multi-line update, try this:
    # User.objects.filter(id=id).update(your params)
    u = User.objects.get(id=id)
    u.first_name = request.POST['first_name']
    u.last_name = request.POST['last_name']
    u.email = request.POST['email']
    u.save()
    return redirect('/')
   
