from rest_framework import serializers
from departments.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Department JSON serializer"""

    class Meta:
        model = Department
        fields = ('code', 'name','dept_head')


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee JSON serializer"""

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        employee.save()
        return employee