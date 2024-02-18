"""
Domain models for commodities subdomain
"""
from uuid import UUID
from pydantic import BaseModel


class Commodity(BaseModel):
    id: UUID
    name: str
    verboseName: str
    description: str
    # `product`, `service`
    type: str


class Product(Commodity):
    type = 'product'


class Service(Commodity):
    type = 'service'
