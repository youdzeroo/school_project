from courses_app.models import Course
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']

       #Если данные поступают с фронта валидация сработает но в случае через админку, то валидация не сработает
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Course.object.all(),
        #         fields=['name', 'duration', 'price']
        #     )
        # ]
