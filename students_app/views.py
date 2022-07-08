from students_app.models import Student
from students_app.serializers import StudentSerializer
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer