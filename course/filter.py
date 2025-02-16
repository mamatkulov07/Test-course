from django_filters.rest_framework import FilterSet
from .views import Course


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = ['name', 'descriptions']
