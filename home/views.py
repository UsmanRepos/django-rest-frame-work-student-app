from django.core.paginator import Paginator
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from home.serializers import StudentSerializer, LoginSerializer, RegisterSerializer, PasswordSerializer
from home.models import Student


class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"status":"200","message":"success"}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid():
            return Response(data={"status":"200", "message":"success"}, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    pagination_class=StandardResultsSetPagination
    serializer_class=StudentSerializer
    queryset= Student.objects.all()

    # def list(self, request):
    #     search = request.GET.get('search')
    #     queryset = self.queryset

    #     if search:
    #         queryset = queryset.filter(first_name__startswith = search)

    #     serializer = StudentSerializer(queryset, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'status': '200', 'message':'success'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = RegisterSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = RegisterSerializer(recent_users, many=True)
        return Response(serializer.data)


# class PersonView(APIView):

#     def get_person(self, id):
#         try:
#             person = Person.objects.get(pk=id)
#             return person
#         except Person.DoesNotExist:
#             pass

#     def get(self, request):
#         persons = Person.objects.all()
        # page = request.GET.get('page', 1)
        # page_size = 3
        # paginator = Paginator(persons, page_size)  
        # serializer = PersonSerializer(paginator.page(page), many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def put(self, request):
#         person = self.get_person(id=request.data.get('id'))
#         serializer = PersonSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def patch(self, request):
#         person = self.get_person(id=request.data.get('id'))
#         serializer = PersonSerializer(person, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
        
#     def delete(self, request):
#         person = self.get_person(id=request.data.get('id'))
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def persons(request):
#     if request.method == 'GET':
#         persons = Person.objects.all()
#         serializer = PersonSerializer(persons, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def details(request, id):
#     try:
#         person = Person.objects.get(pk=id)
#     except Person.DoesNotExist:
#         pass

#     if request.method == 'GET':
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     elif request.method == 'PATCH':
#         serializer = PersonSerializer(person, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     elif request.method == 'DELETE':
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

