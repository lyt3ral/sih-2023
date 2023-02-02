from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse

def UserList(request):
    users = User.objects.all() 
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)