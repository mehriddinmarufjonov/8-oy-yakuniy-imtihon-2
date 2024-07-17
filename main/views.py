from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
from rest_framework import generics
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import permissions

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


class CourseAPIViewSet(ModelViewSet):
    """Course API ViewSet: To get, create, update and delete course data"""
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeacherAPIViewSet(ModelViewSet):
    """Teacher API ViewSet: To get, create, update and delete teacher data"""
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    permission_classes = [permissions.IsAdminUser]


class StartCourseAPIViewSet(ModelViewSet):
    """Start Course API ViewSet: To get, create, update and delete started course data"""
    queryset = models.StartCourse.objects.all()
    serializer_class = serializers.StartCourseSerializer
    permission_classes = [permissions.IsAdminUser]


class LessonAPIViewSet(ModelViewSet):
    """Lesson API ViewSet: To get, create, update and delete lesson data"""
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonVideoAPIViewSet(ModelViewSet):
    """Dars videosi API ViewSet: Dars videosi ma'lumotlarini olish, yaratish, yangilash va o'chirish uchun"""
    queryset = models.LessonVideo.objects.all()
    serializer_class = serializers.LessonVideoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Annotation API ViewSet: Get and create annotation data
    (no option to update and delete, because I thought such capabilities should not be in annotation)"""
    queryset = models.Camment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Filter(APIView):
    """Filter APIView: To filter classes according to the word specified in the query parameter"""

    def get(self, request: Request):
        word = str(request.query_params.get('word'))
        lessons = models.Lesson.objects.filter(name__icontains=word)
        return Response({'lessons': serializers.LessonSerializer(lessons, many=True).data})

    permission_classes = [permissions.IsAuthenticated]


class LikeAPIview(APIView):
    permission_classes = [permissions.IsAuthenticated]
    """Like APIView: To like or dislike lessons"""
    """GET request: Like to get the serializer (not the main data)"""

    def get(self, request):
        serializer = serializers.LikeSerializer()
        return Response(serializer.data)

    """POST request: To add a like or dislike or delete an existing like/dislike"""

    def post(self, request: Request):
        serializer = serializers.LikeSerializer(data=request.data)
        serializer.is_valid()

        if serializer.validated_data.get('like') == True:
            value = True
        else:
            value = False
        lesson_id = serializer.validated_data.get('lesson')
        lesson = models.Lesson.objects.get(pk=lesson_id)

        try:
            like = models.Like.objects.get(
                lesson=lesson,
                user=request.user
            )
            like.delete()
        except:
            pass

        models.Like.objects.create(
            lesson=lesson,
            user=request.user,
            like_or_dislike=value
        )

        return Response()


class SendMailAPI(APIView):
    permission_classes = [permissions.IsAdminUser]
    """Sending news to users' email"""

    def get(self, request):
        serializer = serializers.MailSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.MailSerializer(data=request.data)
        serializer.is_valid()

        users = User.objects.all()
        for user in users:
            subject = serializer.validated_data.get('name')
            message = f"Salom {user.username} {serializer.validated_data.get('text')}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)

        return Response({'success': "Yuborildi!!!"})