from django import forms
from .models import ApplyJob , Job

class ApplyForm(forms.ModelForm):
    class Meta():
        model = ApplyJob
        fields = ['name','email','website','apply_file','comment']


class AddJob(forms.ModelForm):
    class Meta():
        model = Job
        fields = '__all__'
        exclude = ('slug','owner')