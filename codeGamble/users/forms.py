from django import forms

class RegisterForm(forms.Form):
    team_name = forms.CharField(label='Name of Team', max_length=100,required=True,
                                        widget=forms.TextInput(attrs={'class':"",'id':'team_name'}))
    first_member = forms.CharField(label='Name of First Member', max_length=100,required=True,
                                        widget=forms.TextInput(attrs={'class':"",'id':'first_member'}))
    second_member = forms.CharField(label='Name of Second Member', max_length=100,required=False,
                                        widget=forms.TextInput(attrs={'class':"",'id':'second_member'}))