from datetime import datetime
from ninja import Schema, Field

class CustomerSchema(Schema):
  name: str
  phone: str
  email: str
  date_of_birth: datetime
  nationality: str

class BusinessSchema(Schema):
  name: str
  owner: str = Field(alias="owner.name")
  category: str
  registration_date: datetime
  location_information: str
  business_age: str = Field(alias="business_age")

class MessageSchema(Schema):
  message: str

class BusinessCreateSchema(Schema):
  owner_id: int
  name: str
  category: str
  registration_date: datetime
  location_information: str
