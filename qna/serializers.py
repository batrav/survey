from django.db import models
from rest_framework import serializers

from .models import Survey


class SurveyFormSerializers(serializers.ModelSerializer):
     class Meta:
        model = Survey
        fields = '__all__'
        