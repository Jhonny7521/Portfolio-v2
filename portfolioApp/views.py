from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import FormView 
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Project
from .forms import ProjectForm

# Create your views here.
def portfolioView(request):

  if not request.user.is_authenticated :
    user = User.objects.get(pk = 2)
  else:
    user = request.user

  projects = Project.objects.all()
  
  all_projects = []

  for project in projects:
    print(project.tasks.all())
    data = {
      'id': project.id,
      'title': project.title,
      'description': project.description,
      'tasks': project.tasks.all(),
      'url': project.url,
      'url_deploy': project.url_deploy,
      'image' : project.image,
    }

    all_projects.append(data)

  context = {
    'user': user,
    'projects': all_projects,
  }
  return render(request, 'portfolio/portfolio.html', context)

class CreateProjectView(LoginRequiredMixin, FormView):
    model = Project
    template_name = "projects/new_project.html"
    form_class = ProjectForm

    def form_valid(self, form):
      data = {
        'title': form.cleaned_data['title'],
        'description': form.cleaned_data['description'],
        'url': form.cleaned_data['url'],
        'url_deploy': form.cleaned_data['url_deploy'],
        'image': form.cleaned_data['image'],
      }
      new_project = Project.objects.create(**data)
      new_project.tasks.set(form.cleaned_data['tasks'])

      return redirect("portfolio")

class UpdateProjectView(LoginRequiredMixin, UpdateView):

  model = Project
  fields = ['title', 'description', 'tasks', 'url', 'url_deploy', 'image']
  template_name = 'projects/edit_project.html'
  success_url = reverse_lazy('portfolio')

class DeleteProjectView(LoginRequiredMixin, DeleteView):

  model = Project
  template_name = 'projects/delete_project.html'
  success_url = reverse_lazy('portfolio')

# @login_required
# def create_project(request):
#   title = 'Crear Proyecto'
#   form = ProjectForm(request.POST or None)
#   print(request.POST)
#   if form.is_valid():
#     form.save()
#     return redirect("portfolio")
  
#   context = {
#     "title": title,
#     "form": form,
#   }
#   return render(request, 'projects/new_project.html', context)

