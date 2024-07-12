from django.urls import path
from .views import *


urlpatterns = [
    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

    path('course/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='Course_list'),
    path('course/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='course_detail'),

    path('module/', ModuleViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='module_list'),
    path('module/<int:pk>/', ModuleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='module_detail'),

    path('lesson/', LessonViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='lesson_list'),
    path('lesson/<int:pk>/', LessonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='lesson_detail'),

    path('enrollment/', EnrollmentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='enrollment_list'),
    path('enrollment/<int:pk>/', EnrollmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='enrollment_detail'),

    path('assignment/', AssignmentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='assignment_list'),
    path('assignment/<int:pk>/', AssignmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='assignment_detail'),

    path('submission/', SubmissionViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='submission_list'),
    path('submission/<int:pk>/', SubmissionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='submission_detail'),

    path('grade/', GradeViewSet.as_view({'get': 'list', 'post': 'create'}), \
         name='grade_list'),
    path('grade/<int:pk>/', GradeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='grade_detail'),

    path('certificate/', CertificateViewSet.as_view({'get': 'list', 'post': 'create'}), \
         name='certificate_list'),
    path('certificate/<int:pk>/', CertificateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='certificate_detail'),



]