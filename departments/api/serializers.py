from rest_framework import serializers
from departments.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Department JSON serializer"""

    class Meta:
        model = Department
        fields = ('code', 'name','dept_head')


class EmployeeSerializer(serializers.ModelSerializer):
    '''
    registration serializer
    '''
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Employee
        fields = ['email','username', 'password','password2']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user