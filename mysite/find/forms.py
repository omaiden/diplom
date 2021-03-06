from .models import Post, Relative, Missing_person, Victim, Image
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['text','post_type_id']
		

	# def save(self):


class RelativeForm(forms.ModelForm):
	class Meta:
		model = Relative
		fields = '__all__'

	# def save(self):
	# 	Relative.objects.create(fullname=self.cleaned_data['fullname'], telephone=self.cleaned_data['telephone'], adress=self.cleaned_data['adress'], email=self.cleaned_data['email'])

class Missing_personForm(forms.ModelForm):
	class Meta:
		model = Missing_person
		fields = '__all__'
		widgets = {
            'birthday': DateInput(),
            'missing_time' : DateInput(),
        }


	# def save(self):
	# 	Missing_person.objects.create(name=self.cleaned_data['name'], nickname=self.cleaned_data['nickname'], birthday=self.cleaned_data['birthday'], missing_place=self.cleaned_data['missing_place'], missing_time=self.cleaned_data['missing_time'], status=self.cleaned_data['status'])


class VictimForm(forms.ModelForm):
	class Meta:
		model = Victim
		fields = '__all__'

		widgets = {
            'date': DateInput(),
        }

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['image',]
			
	# def save(self):
	# 	Image.objects.create(image=self.cleaned_data['image'])

class RegistrationForm(forms.Form):
	fullname = forms.CharField(label="ФИО", max_length=50, initial='')
	username = forms.CharField(label="Логин", max_length=30)
	email = forms.EmailField(label="Эл. почта", initial='xyz@mail.com')
	password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
	password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput())
	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1==password2:
				return password2
		raise forms.ValidationError("Пароли не совпадают")

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError("Логин уже существовал. Выбрайте другой пожалуйста!")

	def save(self):
		User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], first_name=self.cleaned_data['fullname'],password=self.cleaned_data['password1'])




