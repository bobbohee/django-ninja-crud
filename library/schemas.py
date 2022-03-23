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
