from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Interest,Document
#from uploads.core.models import Document


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class InterestForm(forms.ModelForm):
	#options=(
	#	("fiction","fiction"),
	#	("fear","fear"),
	#	("fear1","fear1"),
	#	("fear2","fear2"),
	#	("fear3","fear3"),)
	#Interests=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=options)
	
	class Meta:
		model=Interest
		fields = ('my_field',)
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','author','genre','description', 'document', 'image',)