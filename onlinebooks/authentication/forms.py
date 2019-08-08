from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class PhoneWidget(forms.MultiWidget):
    def __init__(self):
        widgets = [forms.TextInput(), forms.TextInput()]
        super().__init__(widgets)

    def decompress(self, value):
        if value:
            return value.split(" ")
        else:
            return ['', '']    


class PhoneField(forms.fields.MultiValueField):
    widget = PhoneWidget
    def __init__(self):
        fields = (
            forms.fields.CharField(
                error_messages = {'incomplete': 'Please enter a country calling code.' },
                validators = [
                    RegexValidator(r'^[0-9]{1,5}$', 'Enter a valid country calling code.'),
                ],
            ),
            forms.fields.CharField(
                error_messages = {'incomplete': 'Please enter a phone number'},
                validators = [
                    RegexValidator(r'^[0-9]{1,10}$', 'Please enter a valid phone number'),
                ],
            ),
        )

        super().__init__(
            fields = fields,
            require_all_fields = True
        )

    def compress(self, values):
        return ' '.join(values)

class SignUpForm(UserCreationForm):
    address = forms.CharField()
    mobile_no = PhoneField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'autofocus': True,
            'required': True});
        self.fields['last_name'].widget.attrs.update({'required': True})  
        self.fields['email'].widget.attrs.update({'required': True})      