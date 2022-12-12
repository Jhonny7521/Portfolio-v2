from django.urls import path

from portfolioApp.views import portfolioView, CreateProjectView, UpdateProjectView, DeleteProjectView #, create_project

# Segun el documento de django la url correact para que funcion debe ser accounts/login/
urlpatterns = [
    path('', portfolioView, name='portfolio'),
    path('project/create', CreateProjectView.as_view(), name='add_project'),
    path('project/edit/<int:pk>', UpdateProjectView.as_view(), name='edit_project'),
    path('project/delete/<int:pk>', DeleteProjectView.as_view(), name='delete_project'),

]