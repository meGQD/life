from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'expected_death_date']
    
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    birth_date = serializers.DateField(source='user.birth_date')    
    expected_death_date = serializers.DateField(source='user.expected_death_date')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        if user_data:
            instance.user.first_name = user_data.get('first_name')
            instance.user.last_name = user_data.get('last_name')
            instance.user.birth_date = user_data.get('birth_date')
            instance.user.expected_death_date = user_data.get('expected_death_date')
            instance.user.save()

        return instance
