from django.urls import path
from students_app.views import StudentViewSet

urlpatterns = [
    path('', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('student/<int:pk>/', StudentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})),
]
