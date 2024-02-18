"""
Domain models
"""
from uuid import UUID
from pydantic import BaseModel


class Order(BaseModel):
    id: UUID


class Transaction(BaseModel):
    id: UUID
