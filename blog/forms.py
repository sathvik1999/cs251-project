from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Interest,Document,Rate,Community,Advertise
#from uploads.core.models import Document


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in [ 'password1']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class InterestForm(forms.ModelForm):
	
	class Meta:
		model=Interest
		fields = ('my_field',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','author','genre','description', 'document', 'image','public')

class DocumentCForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','author','genre','description', 'document', 'image',)

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('rating',)

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ('name','description',)

class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertise
        fields = ('title','author','genre','description', 'image')
