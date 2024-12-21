from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First name")
    last_name = forms.CharField(max_length=100, label="Last name")
    email = forms.EmailField(max_length=200, label="Email")
    subject = forms.CharField(max_length=250, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")