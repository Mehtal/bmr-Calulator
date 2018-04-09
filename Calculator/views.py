from django.shortcuts import render
from .forms import BmrForm
# Create your views here.


def bmrvalue(age ,height ,weight , gender ):
	if gender == 'm':
		BMR = (10 * weight ) + (6.25 * height ) - (5 * age ) + 5
	else:
		BMR = (10 * weight ) + (6.25 * height ) - (5 * age ) - 161
	return BMR 



def MyBmr(request):
	if request.method == "POST":
		form = BmrForm(request.POST)
		if form.is_valid():
			age    = form.cleaned_data['age']
			height = form.cleaned_data['height']
			weight = form.cleaned_data['weight']
			gender = form.cleaned_data['gender']
			mybmr  = bmrvalue(age,height,weight,gender)
			
			return render (request , 'resultes.html', {'bmr':mybmr })
	else:
		form = BmrForm()

	return render (request , 'home.html' , {'form': form})