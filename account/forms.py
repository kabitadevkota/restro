from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmailValidationField(forms.EmailField):
    def validate(self,value):
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Email already Exists")
        except User.MultipleObjectsReturned as e:
            raise forms.ValidationError("Email already Exists.")
        except User.DoesNotExist as e:
            pass




class UserSignUpForm(UserCreationForm):
    email = EmailValidationField(required=True)
    class Meta:
        model = User
        fields =('first_name','last_name','email','username',)