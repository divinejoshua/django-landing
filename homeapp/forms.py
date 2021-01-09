from django import forms
from . import models

class visitorForm(forms.ModelForm):
	class Meta:
		model = models.Visitor
		exclude = [ 'ip', 'date', 'country']



