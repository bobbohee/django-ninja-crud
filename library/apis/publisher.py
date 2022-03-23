from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from library.models import Publisher
from library.schemas import PublisherIn, PublisherOut

router = Router(tags=["publisher"])


@router.get("/", response=List[PublisherOut])
def list_publishers(request):
    return Publisher.objects.all()


@router.post("/", response=PublisherOut)
def create_publisher(request, payload: PublisherIn):
    return Publisher.objects.create(**payload.dict(exclude_unset=True))


@router.get("/{id}/", response=PublisherOut)
def get_publisher(request, id: int):
    return get_object_or_404(Publisher, pk=id)


@router.put("/{id}/", response=PublisherOut)
def update_publisher(request, id: int, payload: PublisherIn):
    publisher = get_object_or_404(Publisher, pk=id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(publisher, attr, value)
    publisher.save()
    return publisher


@router.delete("/{id}/", response={204: None})
def delete_publisher(request, id: int):
    publisher = get_object_or_404(Publisher, id=id)
    publisher.delete()
    return 204, None
