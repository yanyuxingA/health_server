from rest_framework import serializers

from users.models import Record


class HealthSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField()
    user_address = serializers.CharField()
    user_age = serializers.IntegerField()
    user_temperature = serializers.FloatField()

    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ['user_name', 'user_age', 'user_temperature', 'user_address']
