from django.forms import ModelForm
from .models import Poll

class CreateForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'firstOption', 'secondOption', 'thirdOption']