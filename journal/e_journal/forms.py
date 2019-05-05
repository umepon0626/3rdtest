from django.forms import ModelForm
from .models import E_journal

class journal_form(ModelForm):
    class Meta:
        model = E_journal
        fields = ['title','text','photo']

