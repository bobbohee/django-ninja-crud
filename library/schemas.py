from ninja import Schema


class PublisherIn(Schema):
    name: str


class PublisherOut(Schema):
    id: int
    name: str
