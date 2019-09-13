from django import forms

Choice_Type = (
    ()
)

class onboard_form(forms.Form):
    manager_name = forms.CharField(max_length=100, label='Name', required=True, help_text='Please enter your name here')
    company_name = forms.CharField(max_length=100, label='Company Name', required=True, help_text='Please enter the name of your company')
    company_type = forms.ChoiceField(choices=Choice_Type, label='Type of Company', initial='', help_text='Select the most relevant option about the working of your company')
    contact_no = forms.CharField(max_length=10, label='Phone Number', required=True, help_text='Please enter your ')
    email_id = 