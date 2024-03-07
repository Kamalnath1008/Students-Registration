from django import forms
from students_app.models import Students

class StudentsForm(forms.ModelForm):
    
    gen=[('male','Male'),('female','Female')]
    gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    bgroup=[('o+ive','O+ive'),('b+ive','B+ive'),('a+ive','A+ive'),('o-ive','O-ive'),('a-ive','a-ive'),('b-ive','b-ive'),('ab+ive','AB+ive'),('ab-ive','AB-ive'),('other','OTHER')]
    Bloodgroup=forms.ChoiceField(choices=bgroup,widget=forms.Select)
    class Meta:
        fields="__all__"
        model=Students