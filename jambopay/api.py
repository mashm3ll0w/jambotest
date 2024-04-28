from ninja import NinjaAPI
from jambopay.models import Customer, Business
from jambopay.schema import CustomerSchema, BusinessSchema, MessageSchema

api = NinjaAPI()

# Get all Customers
@api.get("/customers", response=list[CustomerSchema])
def customers(request):
  return Customer.objects.all()

# Get a specific Customer
@api.get("/customers/{customer_id}", response={200: CustomerSchema, 404: MessageSchema})
def customer(request, customer_id):
  try:
    customer = Customer.objects.get(pk=customer_id)
    return 200, customer
  except Customer.DoesNotExist:
    return 404, {"message": "Customer not found"}

# Create a new Customer
@api.post("/customers", response={201: CustomerSchema})
def create_customer(request, customer: CustomerSchema):
  Customer.objects.create(**customer.dict())
  return customer

# Edit a Customer's details
@api.put("/customers/{customer_id}", response={200: CustomerSchema, 404: MessageSchema})
def update_customer(request, customer_id: int, data: CustomerSchema):
  try:
    customer = Customer.objects.get(pk=customer_id)
    for attribute, value in data.dict().items():
      setattr(customer, attribute, value)
    customer.save()
    return 200, customer
  except Customer.DoesNotExist:
    return 404, {"message": "Customer not found"}

# Delete a Customer
@api.delete("/customers/{customer_id}", response={204: MessageSchema, 404: MessageSchema})
def delete_customer(request, customer_id):
  try:
    customer = Customer.objects.get(pk=customer_id)
    customer.delete()
    return 204, {"message": "Customer successfully deleted!"}
  except Customer.DoesNotExist:
    return 404, {"message": "Customer not found"}

# Get all Businesses
@api.get("/businesses", response=list[BusinessSchema])
def businesses(request):
  return Business.objects.all()

# Get a specific business
@api.get("/businesses/{business_id}", response={200: BusinessSchema, 404: MessageSchema})
def business(request, business_id):
  try:
    business = Business.objects.get(pk=business_id)
    return 200, business
  except Business.DoesNotExist:
    return 404, {"message": "Business not found"}
