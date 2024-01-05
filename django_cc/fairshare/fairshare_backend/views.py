from django.http import HttpResponse
from django.db import connection
from .models import BlogPost
from .models import Users
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return HttpResponse("Hello, world! testing")

def get_users(request):
  users = Users.objects.all()
  user_list = list(users.values('id', 'email', 'name', 'date_joined')) 
  return JsonResponse(user_list, safe=False)

@csrf_exempt
def new_user(request):
  data = json.loads(request.body)
  print(data)
  new_user = Users(email=data['email'], name=data['name'])
  new_user.save()
  return HttpResponse(f"New user created with id {new_user.id}")

