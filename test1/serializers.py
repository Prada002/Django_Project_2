from rest_framework import serializers
from .models import DataList , Depart

class DataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataList
        fields = ['id', 'name', 'roll_no', 'email', 'dept']

    def create(self, validated_data):
        # Create and return a new DataList instance given the validated data
        return DataList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update and return an existing DataList instance given the validated data
        instance.name = validated_data.get('name', instance.name)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.email = validated_data.get('email', instance.email)
        
        # Assuming 'dept' is a ForeignKey to the 'Depart' model
        instance.dept = validated_data.get('dept', instance.dept)

        instance.save()
        return instance

class DepartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depart
        fields = ['id', 'dept']

    def update(self, instance, validated_data):
        # Assuming 'dept' is a ForeignKey to the 'Depart' model
        instance.dept = validated_data.get('dept', instance.dept)
        instance.save()
        return instance
