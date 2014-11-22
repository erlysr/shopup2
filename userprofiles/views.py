from django.views.generic import TemplateView, FormView, RedirectView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from .forms import UserCreationEmailForm, EmailAuthenticationForm, LoginForm, ProfileSignUpForm


# Create your views here.
# No esta en funcionamiento hay que arreglarlo
def register_profile(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		profile_form = ProfileSignUpForm(data=request.POST)
		if profile_form.is_valid:
			profile = profile_form.save()
			registered = True
		else:
			print profile_form.errors
	else:
		profile_form = ProfileSignUpForm

	return render_to_response(
		'ProfileSignUp.html', {'profile_form': profile_form, 'registered': registered}, context
		)
	
def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

	# Aqui loguear el usuario
	# Crear el userprofile, con avatar y todo eso
	# redireccionar al home

	return render(request, 'signup.html', {'form': form})

def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		#loguear
		login(request, form.get_user())

		#redireccionar al home

	return render(request, 'signin.html', {'form': form})

def logout_view(request):
	logout(request)

	#Redireccionar al login page
	return HttpResponseRedirect('/login/')


class ProfileView(TemplateView):
	template_name = 'login_in.html'
	

	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		is_auth = False
		name = None
		lastname = None
		url_avatar = None

		if self.request.user.is_authenticated():
			is_auth = True
			name = self.request.user.first_name
			lastname = self.request.user.last_name
			

			data = {
			'is_auth': is_auth,
			'name': name,
			'lastname': lastname,
			'userprofile': self.get_userprofile()
			}

			context.update(data)

			if self.get_userprofile() == None:
				self.template_name = 'ProfileSignUp.html'

			return context

	def get_userprofile(self):
		try:
			userprofile = self.request.user.userprofile
		except:
			userprofile = None

		return userprofile

class LoginView(FormView):
		form_class = EmailAuthenticationForm
		template_name = 'login.html'
		success_url = '/profile/'

		def form_valid(self, form):
			#email = form.cleaned_data['email']
			#password = form.cleaned_data['password']
			#user = authenticate(email=email, password=password)

			
			#falta validar si el usuario tiene userprofile o si no hay sesion

			login(self.request, form.user_cache)

			admin = form.user_cache.is_superuser
			if  admin:
				self.success_url = '/admin/'

			
			return super(LoginView, self).form_valid(form)


		def get_context_data(self, **kwargs):
			context = super(LoginView, self).get_context_data(**kwargs)
			is_auth = False
			name = None
			lastname = None
			url_avatar = None

			if self.request.user.is_authenticated():
				is_auth = True
				name = self.request.user.first_name
				lastname = self.request.user.last_name

				data = {
				'is_auth': is_auth,
				'name': name,
				'lastname': lastname,
				'userprofile': self.get_userprofile()
				}
				if self.get_userprofile() == None:
				#	self.template_name = 'profilesignup.html'
					self.success_url = '/profilesignup/'
				
				

				context.update(data)

			return context

		def get_userprofile(self):
			try:
				userprofile = self.request.user.userprofile
			except:
				userprofile = None

			return userprofile

class PerfilRedirectView(RedirectView):
	pattern_name = 'perfil' 

class ProfileSignUpView(FormView):
	form_class = ProfileSignUpForm
	template_name = 'ProfileSignUp.html'
	success_url = '/profile/'



























