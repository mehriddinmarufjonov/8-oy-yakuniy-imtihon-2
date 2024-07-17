from . import models
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    """Course uchun serializer"""
    class Meta:
        model = models.Course
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    """Teacher uchun serializer"""
    class Meta:
        model = models.Teacher
        fields = '__all__'


class StartCourseSerializer(serializers.ModelSerializer):
    """Start Course uchun serializer"""
    class Meta:
        model = models.StartCourse
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Lesson uchun serializer"""
    class Meta:
        model = models.Lesson
        fields = '__all__'


class LessonVideoSerializer(serializers.ModelSerializer):
    """Lesson video uchun serializer"""
    class Meta:
        model = models.LessonVideo
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer: Annotate a lesson"""
    class Meta:
        model = models.Camment
        fields = '__all__'

class LikeSerializer(serializers.Serializer):
    """Like serializer: to like or dislike the lesson"""
    lesson = serializers.IntegerField()
    like = serializers.BooleanField()
    dislike = serializers.BooleanField()


class MailSerializer(serializers.Serializer):
    """Mail Serializer: sending news to users' email"""
    name = serializers.CharField(max_length=255)
    text = serializers.CharField()