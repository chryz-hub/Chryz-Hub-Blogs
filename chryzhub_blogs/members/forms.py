from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from blog_app.models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__ (self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'

class EditAccountForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'bio', 'website_url', 'twitter_url', 'github_url',
                    'linkedin_url', 'dribble_url', 'figma_url', 'codepen_url', 'facebook_url',
                        'instagram_url']

        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
            'github_url':forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
            'dribble_url':forms.TextInput(attrs={'class':'form-control'}),
            'figma_url':forms.TextInput(attrs={'class':'form-control'}),
            'codepen_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
        }

