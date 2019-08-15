from django import forms


class place_order(forms.Form):
    customer_name = forms.CharField(max_length=100, label='Name', required=True, help_text='Person for whom this order is being placed')
    customer_no = forms.RegexField(regex=r'^\d{10,10}$', label='Phone Number', required=True, error_message='Only 10 digts allowed' ,help_text='Customer 10 digit Phone number')
    customer_email_id = forms.EmailField(label='Email ID')
    source = forms.CharField(max_length=300, label='Source', required=True, help_text='Descriptive Address of place where order would be loaded')
    destination = forms.CharField(max_length=300, label='Destination', required=True, help_text='Descriptive address of place where order would be delivered')
    weight = forms.DecimalField(max_digits=9, decimal_places=3, label='Weight(Kg)', required=True, help_text='Put approximate weight of the order in Kilograms')
    order_type = forms.MultipleChoiceField(choices=type_choices, label='Attributes of')