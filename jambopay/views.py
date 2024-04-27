from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Customer, Business
from .forms import CustomerForm, BusinessForm
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
  return JsonResponse({"message": "Welcome to the test application",
                       "routes": {
                         "customers": "/customers",
                         "customer": "/customers/id",
                         "businesses": "/businesses",
                         "business": "/businesses/id"
                         }})

#exempt the csrf only because I am testing with POSTMAN, otherwise, do not do this
@csrf_exempt
@require_http_methods(["GET", "POST"])
def customers(request):
  """
  Return a list of all customers currently registered or create a new customer
  """
  if request.method == "GET":
    customers = Customer.objects.all()
    return JsonResponse({"customers": [model_to_dict(customer) for customer in customers]})
  elif request.method == "POST":
    data = request.POST
    form = CustomerForm(data)
    print(form)
    if form.is_valid():
      customer = form.save()
      return JsonResponse(model_to_dict(customer), status=201)
    else:
        return JsonResponse(form.errors, status=400)



#exempt the csrf only because I am testing with POSTMAN, otherwise, do not do this
@csrf_exempt
@require_http_methods(["GET", "PATCH", "DELETE"])
def customer(request, pk):
  """
  Return, edit or delete the details of a single customer by their primary_key
  """
  try:
    customer = Customer.objects.get(pk=pk)
  except Customer.DoesNotExist:
    return JsonResponse({"error": "Customer not found!"}, status=404)

  if request.method == "GET":
    return JsonResponse(model_to_dict(customer))
  elif request.method == "DELETE":
    customer.delete()
    return JsonResponse({"message": "Customer deleted"}, status=204)


#exempt the csrf only because I am testing with POSTMAN, otherwise, do not do this
@csrf_exempt
@require_http_methods(["GET", "POST"])
def businesses(request):
  """
  Returns a list of all businesses and their related owners or creates a new business
  """
  if request.method == "GET":
    businesses = Business.objects.select_related("owner").all()
    businesses_data = [{"id": business.id,
                        "name": business.name,
                        "owner": business.owner.name,
                        "category": business.category,
                        "registration_date": business.registration_date,
                        "business_age": business.business_age} for business in businesses]
    return JsonResponse({"businesses": businesses_data}, safe=False)
  elif request.method == "POST":
    data = request.POST
    form = BusinessForm(data)
    if form.is_valid():
        business = form.save()
        return JsonResponse({"id": business.id,
                        "name": business.name,
                        "owner": business.owner.name,
                        "category": business.category,
                        "registration_date": business.registration_date,
                        "business_age": business.business_age}, status=201)
    else:
        return JsonResponse(form.errors, status=400)


#exempt the csrf only because I am testing with POSTMAN, otherwise, do not do this
@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def business(request, pk):
  """
  Returns a the details of a single business, including the owner
  """
  try:
    business = Business.objects.select_related("owner").get(pk=int(pk))
  except Business.DoesNotExist:
    return JsonResponse({"error": "Business not found"}, status=404)

  if request.method == "GET":
    business_data = model_to_dict(business)
    business_data["owner"] = business.owner.name
    business_data["business_age"] = business.business_age
    return JsonResponse(business_data)
  elif request.method == "DELETE":
    business.delete()
    return JsonResponse({"message": "Business deleted"}, status=204)

