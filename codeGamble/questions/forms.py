from django import forms

class AnswerForm(forms.Form):
    file = forms.FileField(required=True,label="Output File",widget=forms.FileInput(attrs={'class':"inputfile",'id':'output_file'}))