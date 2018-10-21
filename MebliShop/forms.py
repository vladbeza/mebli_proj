from django import forms
from phonenumber_field.formfields import PhoneNumberField

class AddPhoneNumber(forms.Form):
    phone = PhoneNumberField(label="Номер")

class CheaperForm(forms.Form):
    model = forms.CharField(label="Модель", max_length=50)
    where = forms.CharField(label="Где Нашли", max_length=100)
    price = forms.CharField(label="Цена", max_length=20)
    name = forms.CharField(label="ФИО", max_length=100)
    email = forms.EmailField(label="E-Mail")
    phone = PhoneNumberField(label="Номер телефона", widget=forms.TextInput(attrs={'placeholder': '+38(063)3925359'}))
    comment = forms.CharField(label="Примечание", required=False, max_length=500, widget=forms.Textarea())
