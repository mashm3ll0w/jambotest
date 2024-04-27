from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Customer, Business

# Create your views here.

def index(request):
  return JsonResponse({"message": "Welcome to the test application",
                       "routes": {
                         "customers": "/customers",
                         "customer": "/customer/id",
                         "businesses": "/businesses",
                         "business": "/business/id"
                         }})

def customers(request):
  """
  Return a list of all customers currently registered
  """
  customers = Customer.objects.all()
  return JsonResponse({"customers": [model_to_dict(customer) for customer in customers]})

def customer(request, pk):
  """
  Return the details of a single customer by their primary_key
  """
  try:
    customer = Customer.objects.get(pk=pk)
    return JsonResponse(model_to_dict(customer))
  except Customer.DoesNotExist:
    return JsonResponse({"error": "Customer not found!"}, status=404)

def businesses(request):
  """
  Returns a list of all businesses and their related owners
  """
  businesses = Business.objects.select_related('owner').all()
  businesses_data = [{'name': business.name,
                      'owner': business.owner.name,
                      'category': business.category,
                      'registration_date': business.registration_date,
                      'business_age': business.business_age} for business in businesses]
  return JsonResponse({'businesses': businesses_data}, safe=False)

def business(request, pk):
  """
  Returns a the details of a single business, including the owner
  """
  try:
      business = Business.objects.select_related('owner').get(pk=pk)
      business_data = model_to_dict(business)
      business_data['business_age'] = business.business_age
      return JsonResponse(business_data)
  except Business.DoesNotExist:
      return JsonResponse({'error': 'Business not found'}, status=404)
