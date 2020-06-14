from django import forms
from django.forms import Form,ModelForm,Textarea,TextInput,DateInput,TimeInput,CharField,CheckboxSelectMultiple

from .models import Question,Choice

class  QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('pub_date','creator')
        labels = {
            'question_text': 'Card Text',
            'color_text': 'Card Color',
        }    
        widgets = {
            'question_text': Textarea(attrs={"rows":10,'class':'styled-textarea'}),
        }

class  ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        exclude = ('voters',)
        labels = {
            'question': 'Card',
            # 'voters': 'Voters',
            'choice_text': 'Choice',
        }    
       
