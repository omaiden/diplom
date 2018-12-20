from django.contrib.auth.models import Group, User, Permission
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from .forms import PostForm, RegistrationForm, RelativeForm, Missing_personForm, VictimForm, ImageForm
from .models import Victim, Post,Image
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
	return render(request,'index.html')


def login(request):
    return render(request,'login.html')


def regis(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form =RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/index')
	return render(request,'regis.html', {'form':form})


def missing(request):
	if request.method == 'POST':

		form1 = PostForm(request.POST)
		form3 = RelativeForm(request.POST)
		form2 = Missing_personForm(request.POST)
		form4 = ImageForm(request.POST, request.FILES)
		if (form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid()):
			missing_obj = form2.save()
			relative_obj = form3.save()
			image_obj = form4.save(commit=False)
			image_obj.person_id = missing_obj
			image_obj.save()
			post_obj = form1.save(commit=False)
			post_obj.missing_person_id = missing_obj
			post_obj.relative_id = relative_obj
				#victim_obj = Victim.objects.create(date='2018-12-18',place='dacfds')
				#post_obj.victim_id = victim_obj
			post_obj.save()

			return HttpResponseRedirect('/thanks')

	else:
		form1 = PostForm(initial = {'text': 'Этот текст будет разместить на странице чтобы другие ползователи могут увидеть.'})
		form2 = Missing_personForm()
		form3 = RelativeForm()
		form4 = ImageForm()
		#form5 = VictimForm()
	return render(request,'post.html', {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})


def victim(request):
	form1 = PostForm(initial = {'text': 'Этот текст будет разместить на странице чтобы другие ползователи могут увидеть.'})
	form2 = VictimForm()
	form3 = RelativeForm()
	if request.method == 'POST':
		return HttpResponseRedirect('/thanks')
		form1 = PostForm(request.POST)
		form3 = RelativeForm(request.POST)
		form2 = VictimForm(request.POST, request.FILES)
		if (form1.is_valid() and form2.is_valid() and form3.is_valid()):
			vitim_obj = form2.save()
			relative_obj = form3.save()
			post_obj = form1.save(commit=False)
			post_obj.missing_person_id = missing_obj
			post_obj.relative_id = relative_obj
				#victim_obj = Victim.objects.create(date='2018-12-18',place='dacfds')
				#post_obj.victim_id = victim_obj
			post_obj.save()

			return HttpResponseRedirect('/thanks')

	else:
		form1 = PostForm(initial = {'text': 'Этот текст будет разместить на странице чтобы другие ползователи могут увидеть.'})
		form2 = VictimForm()
		form3 = RelativeForm()


	return render(request,'post_victim.html', {'form1': form1, 'form2': form2, 'form3': form3})

def thanks(request):
	return render_to_response('thanks.html')


def image(request):
	i = get_object_or_404(Image, pk=11)
	return render(request, 'image.html', {'image': i})




class PostList(ListView):
	model = Post

