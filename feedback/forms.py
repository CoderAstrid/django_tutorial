from bootstrap_datepicker_plus import DatePickerInput
from django.forms import ModelForm
from .models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'email', 'comment', 'createDate']
        widgets = {
            'createDate': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }
