from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TaskModel


# class Signupform(UserCreationForm):
#     class Meta:
       
#         model=User
#         fields=['username','password1','password2']

#     def __init__(self,*args,**kwargs):
#         super(Signupform,self).__init__(*args,**kwargs)
#         self.fields['username'].widget.attrs['class']='form-control'
#         self.fields['password1'].widget.attrs['class']='form-control'
#         self.fields['password2'].widget.attrs['class']='form-control'




class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

    def __init__(self,*args,**kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'


class TodoForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields=['name','description']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control border-secondary my-3'}),
            'description':forms.TextInput(attrs={'class':'form-control border-secondary my-3'})
        }
