from courses_app.models import Course
from courses_app.serializers import CourseSerializer
from rest_framework import viewsets

"""Information about courses"""


class CourseViewSet(viewsets.ReadOnlyModelViewSet): #ReadOnlyModelViewSet - это для того чтобы фронендчик не мог внести изменений
    queryset = Course.objects.all()  # эта переменная встроенная не может быть измененен потому что под копотом она так и называется. И через эту переменную мы получаем все данные из указанной таблицы
    serializer_class = CourseSerializer # и эта переменная встроенная она принимает нашу функцию сериалайзер и все данные проводит по указанному методу
