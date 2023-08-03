from django.forms import ModelForm
from .models import Review

#ModelForms are used to generate inputs, to validate data of the submitted form and to create a model instance.
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'review', 'date']