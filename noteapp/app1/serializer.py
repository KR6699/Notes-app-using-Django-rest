from django.db.models import fields
from rest_framework import serializers
from .models import MyNotes
class myNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyNotes
        fields = '__all__'
