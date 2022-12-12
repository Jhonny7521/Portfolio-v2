from django.shortcuts import redirect
from .forms import NewUserForm, LoginForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView


class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm

  def form_valid(self, form):
      form.save()
      return redirect('login')

# def logout(request):
#   redirect_url = reverse_lazy('portfolio')
#   logout_then_login(request, redirect_url)

class LoginUserView(LoginView):
  form_class = LoginForm
  template_name = "registration/login.html"
  
  
class LogoutUserView(LogoutView):
  next_page = '/'






