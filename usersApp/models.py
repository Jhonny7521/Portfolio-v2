from django.db import models

# Create your models here.
# class Users(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     username = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)

#     class Meta:
#       db_table="users"

class SideVisits(models.Model):
  ip_address = models.CharField(max_length=20)
  city = models.CharField(max_length=30, default='', null=True)
  country = models.CharField(max_length=30, default='', null=True)
  country_code = models.CharField(max_length=5, default='', null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table="visits"
  
  def __str__(self):
    return self.ip_address