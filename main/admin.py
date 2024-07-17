from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'durationn')
    list_display_links = ('id', 'name')

    def durationn(self, obj):
        return f"{obj.duration} oy"


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'phone', 'experiencee', 'get_image')
    list_display_links = ('id', 'user', 'full_name')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="50px;">')
        return "No Image"

    def experiencee(self, obj):
        return f"{obj.experience} yil"


@admin.register(models.StartCourse)
class StartCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'teacher', 'start', 'end')
    list_display_links = ('id', 'course')


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'name', 'time')
    list_display_links = ('id', 'course')


@admin.register(models.LessonVideo)
class LessonVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'get_video')
    list_display_links = ('id', 'lesson')

    def get_video(self, obj):
        if obj.video:
            return mark_safe(
                f'<video width="50" controls><source src="{obj.video.url}" type="video/mp4">Your browser does not support the video tag.</video>')
        return "No Video"


@admin.register(models.Camment)
class CammentAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'author')
    list_display_links = ('id', 'lesson')


@admin.register(models.Like)
class LiketAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'user', 'like_or_dislike')
    list_display_links = ('id', 'lesson')