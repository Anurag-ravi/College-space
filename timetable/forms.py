from django import forms
from .models import Monday,Tuesday,Wednesday,Thursday,Friday

class MondayUpdateForm(forms.ModelForm):
    eight_nine = forms.CharField(max_length = 5,label="") 
    nine_ten = forms.CharField(max_length = 5,label="") 
    ten_eleven = forms.CharField(max_length = 5,label="") 
    eleven_twelve = forms.CharField(max_length = 5,label="") 
    twelve_one = forms.CharField(max_length = 5,label="") 
    two_three = forms.CharField(max_length = 5,label="")
    three_four = forms.CharField(max_length = 5,label="")
    four_five = forms.CharField(max_length = 5,label="")
    five_six = forms.CharField(max_length = 5,label="")

    class Meta:
        model = Monday
        fields = ['eight_nine','nine_ten','ten_eleven','eleven_twelve','twelve_one','two_three','three_four','four_five','five_six']

class TuesdayUpdateForm(forms.ModelForm):
    eight_nine = forms.CharField(max_length = 5,label="") 
    nine_ten = forms.CharField(max_length = 5,label="") 
    ten_eleven = forms.CharField(max_length = 5,label="") 
    eleven_twelve = forms.CharField(max_length = 5,label="") 
    twelve_one = forms.CharField(max_length = 5,label="") 
    two_three = forms.CharField(max_length = 5,label="")
    three_four = forms.CharField(max_length = 5,label="")
    four_five = forms.CharField(max_length = 5,label="")
    five_six = forms.CharField(max_length = 5,label="")

    class Meta:
        model = Tuesday
        fields = ['eight_nine','nine_ten','ten_eleven','eleven_twelve','twelve_one','two_three','three_four','four_five','five_six']

class WednesdayUpdateForm(forms.ModelForm):
    eight_nine = forms.CharField(max_length = 5,label="") 
    nine_ten = forms.CharField(max_length = 5,label="") 
    ten_eleven = forms.CharField(max_length = 5,label="") 
    eleven_twelve = forms.CharField(max_length = 5,label="") 
    twelve_one = forms.CharField(max_length = 5,label="") 
    two_three = forms.CharField(max_length = 5,label="")
    three_four = forms.CharField(max_length = 5,label="")
    four_five = forms.CharField(max_length = 5,label="")
    five_six = forms.CharField(max_length = 5,label="")

    class Meta:
        model = Wednesday
        fields = ['eight_nine','nine_ten','ten_eleven','eleven_twelve','twelve_one','two_three','three_four','four_five','five_six']

class ThursdayUpdateForm(forms.ModelForm):
    eight_nine = forms.CharField(max_length = 5,label="") 
    nine_ten = forms.CharField(max_length = 5,label="") 
    ten_eleven = forms.CharField(max_length = 5,label="") 
    eleven_twelve = forms.CharField(max_length = 5,label="") 
    twelve_one = forms.CharField(max_length = 5,label="") 
    two_three = forms.CharField(max_length = 5,label="")
    three_four = forms.CharField(max_length = 5,label="")
    four_five = forms.CharField(max_length = 5,label="")
    five_six = forms.CharField(max_length = 5,label="")

    class Meta:
        model = Thursday
        fields = ['eight_nine','nine_ten','ten_eleven','eleven_twelve','twelve_one','two_three','three_four','four_five','five_six']

class FridayUpdateForm(forms.ModelForm):
    eight_nine = forms.CharField(max_length = 5,label="") 
    nine_ten = forms.CharField(max_length = 5,label="") 
    ten_eleven = forms.CharField(max_length = 5,label="") 
    eleven_twelve = forms.CharField(max_length = 5,label="") 
    twelve_one = forms.CharField(max_length = 5,label="") 
    two_three = forms.CharField(max_length = 5,label="")
    three_four = forms.CharField(max_length = 5,label="")
    four_five = forms.CharField(max_length = 5,label="")
    five_six = forms.CharField(max_length = 5,label="")

    class Meta:
        model = Friday
        fields = ['eight_nine','nine_ten','ten_eleven','eleven_twelve','twelve_one','two_three','three_four','four_five','five_six']

