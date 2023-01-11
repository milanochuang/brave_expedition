from django import forms


class CreateNewList(forms.Form):
	name = forms.CharField(label = "Name", max_length = 200)
	check = forms.BooleanField(required = False)
	
class CreateNewFeatures(forms.Form):
	NewFeatures = forms.CharField(label="NewFeatures", max_length=200)
	checking = forms.BooleanField(required=False)