from django import forms
from apps.contacts.models import Contact


class EditForm(forms.ModelForm):

    name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    contacts = forms.CharField()
    other_contacts = forms.CharField(max_length=100,
                                     widget=forms.Textarea, required=False)
    bio = forms.CharField(max_length=1000, widget=forms.Textarea,
                          required=False)

    class Meta:
        model = Contact
        fields = ['name', 'contacts', 'last_name', 'email', 'date_of_birth',
                  'skype', 'photo', 'jabber', 'other_contacts', 'bio']
