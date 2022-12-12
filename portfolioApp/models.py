from django.db import models

# Create your models here.
class Task(models.Model):
  name = models.CharField(max_length=20)
  image = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta:
    db_table = 'tasks'


class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  url = models.URLField(max_length=200)
  url_deploy = models.URLField(max_length=200, default='')
  image = models.CharField(max_length=200)
  tasks = models.ManyToManyField(Task)
  created_at = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.title

  class Meta:
    db_table = "projects"