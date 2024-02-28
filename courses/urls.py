from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from courses.views import HomePageView, CoursePage, SignupView, LoginView, signout, checkout, verifyPayment, MyCoursesList
from coursewebsite.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('', HomePageView.as_view() , name="home"),
    path('logout', signout , name="logout"),
    path('my_courses', MyCoursesList.as_view() , name="my_courses"),
    path('signup', SignupView.as_view() , name="signup"),
    path('login/', LoginView.as_view() , name="login"),
    path('course/<str:slug>', CoursePage , name="CoursePage"),
    path('check-out/<str:slug>', checkout, name="checkout"),
    path('verify_payment', verifyPayment, name="verify_payment"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)