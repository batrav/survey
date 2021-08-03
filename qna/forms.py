from django import forms
from django.db import models
from django.forms import fields

from .models import Survey

class SurveyForm(forms.ModelForm):
    class  Meta:
        model = Survey
        fields = '__all__'
        # labels = {            
        #     'profile_icon': "Profile Icon",
        #     'vaccine_proof': "Proof of Vaccination"        
        # }
        # error_messages = {
        #     "profile_icon": {"required": "your profile must not be empty"},
        #      "vaccine_proof": {"required": "your vaccine must not be empty"}
        # }



