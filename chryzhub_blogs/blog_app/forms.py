from django import forms
from .models import Post, Category

#
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

choices= Category.objects.all().values_list('name', 'name')

choice_list=[]

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=['title', 'snippet', 'category', 'body']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.TextInput(attrs={'class':'form-control', 'placeholder':'What is this blog about concisely!'}),
    }

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields=['name']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
    }

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
