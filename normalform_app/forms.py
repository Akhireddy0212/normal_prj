from django import forms
class Employe_form(forms.Form):
    name = forms.CharField(max_length=50)
    role = forms.CharField(max_length=50)
    salary = forms.CharField(max_length=50)
    age = forms.IntegerField()
    email = forms.EmailField()