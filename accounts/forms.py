from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserCreateForm(UserCreationForm) :
    def __init__(self, *args, **kwargs) :
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class':'form-control'})

class AuthenticateForm(AuthenticationForm) :
    def __init__(self, *args, **kwargs) :
        super(AuthenticateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password']:
            self.fields[fieldname].widget.attrs.update({'class':'form-control'})