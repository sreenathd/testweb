from django import forms

class StressForm(forms.Form):
    CPU = [('1', '1'), ('2', '2'), ('3','3'), ('4','4'), ('5', '5'), ('6', '6'), ('7','7'), ('8','8')]
    TIME = [('10', '10'), ('20', '20'), ('30','30'), ('40', '40'), ('50', '50'), ('60', '60')]
     
    CPU_in_numbers = forms.ChoiceField(choices=CPU, widget=forms.Select())
    Time_in_seconds = forms.ChoiceField(choices=TIME, widget=forms.Select())
