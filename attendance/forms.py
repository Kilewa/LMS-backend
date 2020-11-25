from attendance.api.models import Attendance
from django.forms import formset_factory

class Attendanceform(ModelForm):
    class Meta:
        model = Attendance
        widgets = {'employee' : HiddenInput}
        fields = ('employee','attendance','department_head')

AttendanceFormset = inlineformset_factory(department_head,Attendance,form=Attendanceform,fields=('attendance','employee'))