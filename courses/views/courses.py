from django.http import HttpResponse
from django.shortcuts import render, redirect
from courses.models import Course, Video, course
from courses.models import UserCourse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url="login"), name="dispatch")
class MyCoursesList(ListView):
    template_name = "courses/my_courses.html"
    context_object_name = "user_courses"

    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)
    


'''
@login_required(login_url="login")
def my_courses(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user = user)
    context = {
        "user_courses" : user_courses
    }
    return render(request, template_name="courses/my_courses.html", context = context)
'''
def CoursePage(request, slug):
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    next_number = 2;
    prev_number = None;
    if serial_number is None:
        serial_number = 1
    else:
        next_number = int(serial_number)+1
        if len(videos) < next_number:
            next_number = None

        prev_number = int(serial_number)-1

    video = Video.objects.filter(serial_number = serial_number, course = course) .first()

    if (video.is_preview is False):
        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user  , course = course)
            except:
                return redirect("checkout", slug = course.slug)
    context = {
        "course" : course,
        "video"  : video,
        "videos" : videos,
        "next_number" : next_number,
        "prev_number" : prev_number
    }
    return render(request, template_name="courses/course_page.html", context= context)