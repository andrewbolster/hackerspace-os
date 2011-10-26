import django.forms as forms

from django.contrib.auth.models import User
from django.forms.models import ModelForm

from hos.members.models import ContactInfo


class UserNameForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserEmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',)


class UserAdressForm(ModelForm):

    class Meta:
        model = ContactInfo
        fields = ('street', 'city', 'postcode', 'country')


class UserImageForm(ModelForm):

    class Meta:
        model = ContactInfo
        fields = ('image',)
