from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.core.validators import EmailValidator
from django.utils.safestring import SafeString
from .models import Contact


class CreateContact(forms.Form):
    name = forms.CharField(label="Name", max_length=200, required=True)
    last_name = forms.CharField(label="Last Name", max_length=200, required=True)
    number = forms.IntegerField(label="Telephone", required=True)
    mail = forms.CharField(label="E-Mail", validators=[EmailValidator()], required=True)
    text = forms.CharField(label="Messange", widget=forms.Textarea, required=True)
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'col-md-12'
        self.fields['name'].widget.attrs['placeholder'] = 'Leave your name here!'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Leave your last name here!'
        self.fields['number'].widget.attrs['placeholder'] = 'Leave your number phone here!'
        self.fields['mail'].widget.attrs['placeholder'] = 'Leave your Email here!'
        self.fields['text'].widget.attrs['placeholder'] = 'Leave your message here!'    

    def as_div(self):

        html = []
        for field in self:
            if field == self['text']:
                html.append(f'<label class="col-md-2 col-form-label">{field.label}</label>')
                html.append(f'<div class="col-md-12">{field}</div>')
            else:
                html.append(f'<label class="col-md-2 col-form-label">{field.label}</label>')
                html.append(f'<div class="col-md-12">{field}</div>')
        return SafeString('\n'.join(html))

    def clean_captcha(self):
        response = self.cleaned_data.get('captcha')
        if not response:
            raise forms.ValidationError("Please verify the reCAPTCHA")
        return response

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get('number')
        mail = cleaned_data.get('mail')

        if not number.isdigit():
            raise forms.ValidationError("Please enter a valid phone number")

        if not mail.endswith('@gmail.com'):
            raise forms.ValidationError("Please enter a valid Gmail address")

        return cleaned_data

    def save(self, commit=True):
        if commit:
            contact = Contact.objects.create(
                name=self.cleaned_data['name'],
                last_name=self.cleaned_data['last_name'],
                number=self.cleaned_data['number'],
                mail=self.cleaned_data['mail'],
                text=self.cleaned_data['text']
            )
            return contact
        else:
            return None
