from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

  class Meta:
    model = Project
    fields = ['title', 'description', 'tasks', 'url', 'url_deploy', 'image']
    labels = {
      'title':'Titulo', 
      'description':'Descripción', 
      'tasks':'Tecnologías', 
      'url':'Link',
      'url_deploy': 'Link de despliegue',
      'image':'Url Imagen',
      }
    help_texts = { 
      'tasks':"Presione 'Alt' si desea seleccionar mas de una tecnología",
      }

  #Validaciones personalizada
  def clean_title(self):
    title = self.cleaned_data.get('title')
    if(title == ''):
      raise forms.ValidationError('Este campo no puede estar vacío')
    
    for instancia in Project.objects.all():
      if instancia.title == title:
        raise forms.ValidationError('Ya existe un proyecto llamado' + title)

    return title
