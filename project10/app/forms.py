from django import forms
def validator_for_len(sname):
    if len(sname) < 5:
        raise forms.ValidationError('invalid data')


def validator_for_a(name):
    if name.startswith():
        raise forms.ValidationError('invalid data')



class SkoolForm(forms.Form):
    sname = forms.CharField(max_length=150, required=False, validators=[validator_for_len, validator_for_a])
    princy = forms.CharField(max_length=150, required=False, validators=[validator_for_a])
    pno = forms.CharField(max_length=150, required=False)
    add = forms.CharField(max_length=150, required=False)