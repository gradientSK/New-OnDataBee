from django import forms
from .models import youtube_id


class id_field(forms.ModelForm):
    class Meta:
        model = youtube_id
        fields = [
            'channelid',
        ]
