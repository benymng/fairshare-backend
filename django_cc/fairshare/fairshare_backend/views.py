from django.http import HttpResponse
from django.db import connection
from .models import BlogPost
from .models import Users
from django.utils import timezone
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world! testing")

def new_endpoint(request):
    return HttpResponse("This is a new endpoint")

def test(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")  # Simple SQL query
        row = cursor.fetchone()
    return HttpResponse(f"DB Test: {row}")

def create_entry(request):
  new_post = BlogPost(title='New test', content='Hello world', pub_date=timezone.now())
  new_post.save()
  return HttpResponse(f"New BlogPost created with id {new_post.id}")

def get_blogs(request):
  posts = BlogPost.objects.all()
  posts_list = list(posts.values('id', 'title', 'content', 'pub_date'))  # convert QuerySet to list of dict
  return JsonResponse(posts_list, safe=False)

def get_users(request):
  users = Users.objects.all()
  user_list = list(users.values('id', 'email', 'name', 'date_joined')) 
  return JsonResponse(user_list, safe=False)

