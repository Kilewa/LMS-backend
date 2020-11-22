class Attendanceform(ModelForm):
    class Meta:
        model = Attendance
        widgets = {'employee' : HiddenInput}
        fields = ('employee','attendance','department_head')

AttendanceFormset = inlineformset_factory(Head_of_department,Attendance,form=Attendanceform,fields=('attendance','employee'))