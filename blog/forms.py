from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Interest

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','author','text','genre')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class InterestForm(forms.ModelForm):
	options=(
		("fiction","fiction"),
		("fear","fear"),)
	Interests=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=options)
	
	class Meta:
		model=Interest
		fields = ('Interests',)
