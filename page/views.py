from django.forms import model_to_dict
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from page.serializers import *
from rest_framework.decorators import api_view
from page import models
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, mixins, views
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics, filters

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from page.filters import *


@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    try:
        username = request.data.get('username')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        if not login:
            res = {
                'msg': 'Login empty',
                'status': 0,
            }
            return Response(res)

        user = Customuser.objects.filter(username=username).first()
        if not user:
            user = Customuser.objects.create(
                username=username,
                last_name=last_name,

            )
        elif user:
            if user.complete == 0:
                user.set_password(str(password))
                user.username = username
                user.last_name = last_name

                user.save()

            if user.complete == 1:
                res = {
                    'msg': 'User exits',
                    'status': 2,
                }
            else:
                res = {
                    'msg': 'User exits',
                    'sms': 'The ',
                    'status': 1,
                }
            return Response(res)
        elif password != confirm_password:
            res = {
                'msg': 'Password not equal',
                'status': 2,
            }
            return Response(res)

        user.set_password(str(password))
        user.username = username
        user.last_name = last_name

        user.save()

        if user:
            result = {
                'status': 1,
                'msg': 'registered',
            }
            return Response(result, status=status.HTTP_200_OK)
        else:
            res = {
                'status': 0,
                'msg': 'Can not authenticate with the given credentials or the account has been deactivated'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        if not login:
            res = {
                'msg': 'Login empty',
                'status': 0,
            }
            return Response(res)

        user = Customuser.objects.filter(username=username).first()
        if not user:
            res = {
                'msg': 'username or password wrond',
                'status': 0,
            }
            return Response(res)

        if user and user.check_password(password):
            if user.complete == 0:
                res = {
                    'msg': 'email sms code not check',
                    'status': 0,
                }
                return Response(res)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            refresh = RefreshToken.for_user(user)
            result = {
                'status': 1,
                'user': CustomuserSerializer(user, many=False, context={"request": request}).data,
                'token': token,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response(result, status=status.HTTP_200_OK)


        else:

            res = {
                'status': 0,
                'msg': 'Can not authenticate with the given credentials or the account has been deactivated'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


class TableViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['group_name', 'week']
    search_fields = ['name']
    filterset_class = TableFilter

    def get_serializer_class(self):
        if self.action == "list":
            return TableSerializer
        else:
            return TableSerializer


class GroupDayView(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializers

    # @action(methods=["post"])
    # def


class FanlarView(generics.CreateAPIView):
    queryset = Fanlar.objects.all()
    serializer_class = Fanlarser
