from datetime import date, datetime
from typing import List

from ninja import Schema


class PublisherIn(Schema):
    name: str


class PublisherOut(Schema):
    id: int
    name: str


class AuthorIn(Schema):
    name: str = None
    email: str = None


class AuthorOut(Schema):
    id: int
    name: str
    email: str = None


class BookOut(Schema):
    isbn: str
    name: str
    sub_name: str
    publisher: PublisherOut
    authors: List[AuthorOut]
    price: int
    pages: int
    release_date: date
    create_date: datetime
    update_date: datetime
