from django.urls import path, include
from home.views import StudentViewSet, Register, Login
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    # path('persons', PersonView.as_view()),
    # path('persons/<int:id>', details),
]

