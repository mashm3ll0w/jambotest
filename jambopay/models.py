from django.db import models
from datetime import *
from dateutil import relativedelta
from dateutil.parser import parse


# Create your models here.
class Customer(models.Model):
  """
  Creates a new Customer
  """
  name = models.CharField(max_length=255, null=False, db_index=True)
  phone = models.CharField(max_length=13, null=False)
  email = models.EmailField(null=False)
  date_of_birth = models.DateField(null=False)
  nationality = models.CharField(max_length=50, null=False)

  def __str__(self):
    return self.name


class Business(models.Model):
  """
  Creates a new Business
  """
  owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, null=False, db_index=True)
  category = models.CharField(max_length=255, null=False)
  registration_date = models.DateField(null=False)
  location_information = models.CharField(max_length=255, null=False)

  @property
  def age_of_the_business(self):
    today = date.today()
    reg_date = parse(self.registration_date)
    age = relativedelta.relativedelta(today, reg_date)
    return f"{age.years} Years {age.months} Months {age.days} Days"

  def __str__(self):
      return self.name
