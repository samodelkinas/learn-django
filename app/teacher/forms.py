from django import forms


class QuestionForm(forms.Form):
    text = forms.CharField()
    image = forms.FileField()
