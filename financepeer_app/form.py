from django import forms
import json
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Blog
valid_file = ['json']
class JSONForm(forms.Form):
    file = forms.FileField()

    def clean(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file')
        if not str(file).split('.')[1] in valid_file:
            raise ValidationError("File Not Supported.")

def handleFileUpload(data):
    json_data = json.loads(data)
    for data in json_data:
        if data['userId'] and User.objects.get(id=data['userId']):
            add_blog = Blog.objects.create(userId=User.objects.get(id=data['userId']), title=data['title'], body=data['body'])
            add_blog.save()
        else:
            raise ValidationError("User Doesn't Exist")