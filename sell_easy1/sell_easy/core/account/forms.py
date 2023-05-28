from django import forms
from .models import Profile

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    
class SignUpForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'password')
        exclude =('is_verified', 'is_admin', 'is_staff', 'is_seller', 'surname', 'address', 'phone_number')