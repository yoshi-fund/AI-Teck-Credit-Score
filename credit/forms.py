from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ['outstanding_debt', 'delay_from_due_date', 'num_of_delayed_payment',
                  'interest_rate', 'num_bank_accounts', 'num_of_loan', 'num_credit_card']