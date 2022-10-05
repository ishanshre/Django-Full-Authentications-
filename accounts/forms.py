from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['first_name','last_name','date_of_birth','gender','username','email']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name','date_of_birth','gender','username','email']
        