from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import AllCourses
from django.template import loader


# Create your views here.
def Courses(request):
    ac = AllCourses.objects.all()
    template = loader.get_template('courses.html')
    context = {
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))


def Details(request, course_id):
    try:
        course = AllCourses.objects.get(pk=course_id)
    except AllCourses.DoesNotExist:
        raise Http404("Course not available")
    return render(request, 'details.html', {'course': course})
