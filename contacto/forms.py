from django import forms
# from django_recaptcha.fields import ReCaptchaField
from django.core.validators import EmailValidator


class CreateContact(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200, required=True)
    last_name = forms.CharField(label="Apellido", max_length=200, required=True)
    number = forms.IntegerField(label="Telefono", required=True)
    mail = forms.CharField(label="Email", validators=[EmailValidator()], required=True)
    text = forms.CharField(label="Envia tu Mensaje", widget=forms.Textarea, required=True)
    # captcha = ReCaptchaField()
