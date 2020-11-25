from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AttendanceSerializer
from .models import Attendance
from rest_framework.generics import GenericAPIView
from django.views.generic.edit import CreateView

# Create your views here.


class Attendancecreate(CreateView):
    model = Attendance
    success_url = '/dashboard/'

    def get_context_data(self,** kwargs):
        context = super(Attendancecreate, self).get_context_data(**kwargs)
        context['formset'] = AttendanceFormset(queryset=Attendance.objects.none(), instance=department_head.objects.get(email=self.request.user.email), initial=[{'employee': employee} for employee in self.get_initial()['employee']])
        return context

    def get_initial(self):
        email = self.request.user.email
        head_of_department = department_head.objects.objects.get(email=email)
        initial = super(Attendancecreate , self).get_initial()
        initial['employee'] = Employee.objects.filter(head_of_department=head_of_department)
        return initial

    def post(self, request, *args, **kwargs,):
        formset = AttendanceFormset(request.POST,queryset=Attendance.objects.none(), instance=department_head.objects.objects.get(email=self.request.user.email), initial=[{'employee': employee} for employee in self.get_initial()['employee']])
        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self,formset):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.department_head.objects = get_object_or_404(department_head.objects email=self.request.user.email)
            instance.save()
        return HttpResponseRedirect('/dashboard/')