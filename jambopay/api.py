from ninja import NinjaAPI
from jambopay.models import Customer, Business
from jambopay.schema import CustomerSchema, BusinessSchema, NotFoundSchema

api = NinjaAPI()

@api.get("/customers", response=list[CustomerSchema])
def customers(request):
  return Customer.objects.all()

@api.get("/customers/{customer_id}", response={200: CustomerSchema, 404: NotFoundSchema})
def customer(request, customer_id):
  try:
    customer = Customer.objects.get(pk=customer_id)
    return 200, customer
  except Customer.DoesNotExist:
    return 404, {"message": "Customer not found"}

@api.get("/businesses", response=list[BusinessSchema])
def businesses(request):
  print([business.owner for business in Business.objects.all()])
  return Business.objects.all()

@api.get("/businesses/{business_id}", response={200: BusinessSchema, 404: NotFoundSchema})
def business(request, business_id):
  try:
    business = Business.objects.get(pk=business_id)
    return 200, business
  except Business.DoesNotExist:
    return 404, {"message": "Business not found"}
