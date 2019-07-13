from rest_framework import serializers

class MahasiswaSerializer(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()

class DaftarKuliahSerializer(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
