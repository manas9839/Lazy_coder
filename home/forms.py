from django import forms
from .models import Contact


class contactForm(forms.ModelForm):
    # ! all parameter defined to apply styling over the page
    
    name = forms.CharField(label="Name" ,max_length=100, required=True,widget=forms.TextInput(attrs={"class": "full-width", "placeholder":"Your Name"}),)

    email = forms.EmailField(label="Email" ,max_length=254, required=True,widget=forms.EmailInput(attrs={"class": "full-width", "placeholder":"Your Email"}),)

    website = forms.URLField(label="Website" ,max_length=200, required=False,widget=forms.TextInput(attrs={"class": "full-width", "placeholder":"Website"}),)

    message = forms.CharField(label="Message" ,widget=forms.Textarea(attrs={"class": "full-width", "placeholder": "Your Message"}),) 
    
    phone = forms.CharField(label="Phone number", required=False, widget=forms.TextInput(attrs={"class": "full-width", "placeholder":"Your Phone number with country code (+XX XXX XXX XXXX)", "type": "tel",}),)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'website',  'message',]
