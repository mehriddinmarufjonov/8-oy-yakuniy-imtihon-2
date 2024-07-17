from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseAPIViewSet, TeacherAPIViewSet, StartCourseAPIViewSet, LessonAPIViewSet, LessonVideoAPIViewSet, CommentViewSet, Filter, LikeAPIview, SendMailAPI


router = DefaultRouter()
router.register('course', CourseAPIViewSet) 
router.register('teacher', TeacherAPIViewSet) 
router.register('Startcourse', StartCourseAPIViewSet) 
router.register('lesson', LessonAPIViewSet)
router.register('lessonvideo', LessonVideoAPIViewSet)  
router.register('comments', CommentViewSet)



urlpatterns = [ 
    path('', include(router.urls)),
    path('filter/', Filter.as_view()),
    path('like-or-dislike/', LikeAPIview.as_view()),
    path('send-mail/', SendMailAPI.as_view()),

]