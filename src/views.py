from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import TodoSerializer
from .models import TodoItemAPI
from account.models import User

JWT_authenticator = JWTAuthentication()


class HomeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = JWT_authenticator.authenticate(request)
            if response is not None:
                email_id = response[0]
                ongoing_todo = TodoItemAPI.objects.\
                    filter(user_email=email_id). \
                    filter(deadline_at__gt=timezone.now()). \
                    filter(is_completed=False)
                expired_todo = TodoItemAPI.objects. \
                    filter(user_email=email_id). \
                    filter(deadline_at__lt=timezone.now()). \
                    filter(is_completed=False)
                completed_todo = TodoItemAPI.objects. \
                    filter(user_email=email_id). \
                    filter(is_completed=True)
                response = Response()
                response.data = {
                    'ongoing': TodoSerializer(ongoing_todo, many=True).data,
                    'expired': TodoSerializer(expired_todo, many=True).data,
                    'completed': TodoSerializer(completed_todo, many=True).data
                }
                response.status_code = 200
                return response
            else:
                raise AuthenticationFailed('Invalid token or expired token.')
        except AuthenticationFailed as e:
            print(e)
            raise AuthenticationFailed('Invalid token or expired token.')


class AddToDo(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            email_id = response[0]
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                todo_add = TodoItemAPI(
                    user_email=email_id,
                    title=serializer.data['title'],
                    description=serializer.data['description'],
                    deadline_at=serializer.data['deadline_at']
                )
                todo_add.save()
                return Response({
                    'message': 'Todo added successfully.'
                })
            else:
                raise ValidationError('Invalid form format provided.')
        else:
            raise AuthenticationFailed('Invalid token or expired token.')


class CompleteToDoItem(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            email_id = response[0]
            cmpl_todo = TodoItemAPI.objects.filter(user_email=email_id).filter(id=request.data['id'])
            if cmpl_todo.exists():
                cmpl_todo.update(is_completed=True)
                return Response({
                    'message': 'Todo completed successfully.'
                })
            else:
                raise ValidationError('Invalid Todo ID provided.')
        else:
            raise AuthenticationFailed('Invalid token or expired token.')
