from django.shortcuts import render
import random
import  time
from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
# from django.core.urlresolvers import reverse
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from users.models import Users
from users.serializers import UsersSerializers

# Create your views here.


def indnx(request):
    context = {}
    return render(request, 'indnx.html',context)


class UsersView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers

    # 注册
    @action(detail = False, methods = ['post'], url_path = 'registered')
    def registered(self, request):
        data = request.data
        serializer = self.get_serializer(data = data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status = status.HTTP_200_OK)

    # 登陆
    @action(detail = False, methods = ['post'], url_path = 'login')
    def login(self, request):
        try:
            queryset = self.queryset.get(user_name = request.data['user_name'],
                                         user_password = request.data['user_password'])
            return Response({'message': '用户 {} 登陆成功'.format(queryset.user_name)}, status = status.HTTP_200_OK)
        except EOFError:
            return Response({'message': '用户名或密码错误', 'code': 200})
