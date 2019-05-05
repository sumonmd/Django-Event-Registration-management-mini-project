from django import forms

class TicketForm(forms.Form):
    name = forms.CharField(min_length=2,widget=forms.TextInput(attrs={'class':'input','placeholder':'আপনার পূর্ণ  নাম'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'input','placeholder':'ইমেইল ঠিকানা'}))
    phone = forms.CharField(min_length=11,max_length=11,widget=forms.TextInput(attrs={'class':'input','placeholder':'মোবাইল ফোন নম্বর'}))