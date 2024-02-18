"""
Domain models for wallets subdomain
"""
from uuid import UUID
from pydantic import BaseModel


class Wallet(BaseModel):
    id: UUID
    identity_id: str


class Currency(BaseModel):
    id: UUID
    # `fiat`, `virtual`
    type: str
    # IS O4217: https://en.wikipedia.org/wiki/ISO_4217
    # `USD`, `BTC`, `ETH`, etc
    code: str


class Balance(BaseModel):
    id: UUID
    wallet: Wallet
    currency: Currency
    # TODO: int or float
    balance: float
