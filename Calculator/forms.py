from django import forms
from .models import bmrcalc

class BmrForm(forms.ModelForm):
	class Meta :
		model  = bmrcalc
		fields = ('age','weight','height','gender')
