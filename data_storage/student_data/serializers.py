from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    father_name = serializers.CharField(max_length=255)
    student_id = serializers.CharField(max_length=255)
    contact_number = serializers.CharField(max_length=255)

    def create(self, validated_data):
        # Create and return a new Student instance
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update and return an existing Student instance
        instance.name = validated_data.get('name', instance.name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.student_id = validated_data.get('student_id', instance.student_id)
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        instance.save()
        return instance
