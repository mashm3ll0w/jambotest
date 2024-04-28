from datetime import datetime
from ninja import Schema

class CustomerSchema(Schema):
  name: str
  phone: str
  email: str
  date_of_birth: datetime
  nationality: str

class BusinessSchema(Schema):
  name: str
  owner: CustomerSchema = None
  category: str
  registration_date: datetime
  location_information: str

class NotFoundSchema(Schema):
  message: str
