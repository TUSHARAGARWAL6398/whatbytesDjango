from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username
                self.cleaned_data['username'] = username
            except User.DoesNotExist:
                raise ValidationError("Invalid login")
        return super(LoginForm, self).clean()

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()

class PasswordChangeCustomForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
