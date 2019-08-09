from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe

class PhoneWidget(forms.MultiWidget):
    def __init__(self):
        widgets = [forms.TextInput(attrs={
            'placeholder': 'Country Code: e.g. 91 for India',
            'class': 'form-control'
            }), 
        forms.TextInput(attrs={
            'placeholder': 'Mobile Number',
            'class': 'form-control',
            })]
        super().__init__(widgets)

    def decompress(self, value):
        if value:
            return value.split(" ")
        else:
            return ['', '']  

    def format_output(self, value):
        if value == '' or value is None:
            return None
        if self.is_localized:
            return formats.localize_input(value)
        return str(value)        

    def render(self, name, value, attrs=None, renderer=None):
        if self.is_localized:
            for widget in self.widgets:
                widget.is_localized = self.is_localized
        if not isinstance(value, list):
            value = self.decompress(value)
        output = []
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id', None)
        for i, widget in enumerate(self.widgets):
            try:
                widget_value = value[i]
            except IndexError:
                widget_value = None
            if id_:
                final_attrs = dict(final_attrs, id='%s_%s' % (id_, i))
            output.append(widget.render(name + '_%s' % i, widget_value, final_attrs))
        return [mark_safe(self.format_output(x)) for x in output]        


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
        for field in self.fields:
            if field != 'mobile_no':
                if field == 'password2':
                    self.fields[field].widget.attrs.update({
                        'class': 'form-control',
                        'placeholder': 'Confirm password'
                    })
                elif field == 'password1':
                     self.fields[field].widget.attrs.update({
                        'class': 'form-control',
                        'placeholder': 'Password'
                    })   
                else :    
                    self.fields[field].widget.attrs.update({
                        'class' : 'form-control',
                        'placeholder': field.replace('_', " ").capitalize()
                        })             