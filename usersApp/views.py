from django.shortcuts import redirect, render
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewUserForm, LoginForm
from .models import SideVisits


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


class VisitsView(LoginRequiredMixin, View):

  def get(self, request):
    visits = SideVisits.objects.all().order_by('-pk')
    context = {
      'visits': visits
    }

    return render(request, 'visits/see_visits.html', context)








