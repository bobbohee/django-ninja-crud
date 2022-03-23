from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from library.models import Author
from library.schemas import AuthorIn, AuthorOut

router = Router(tags=["author"])


@router.get("/", response=List[AuthorOut])
def list_authors(request):
    return Author.objects.all()


@router.post("/", response=AuthorOut)
def create_author(request, payload: AuthorIn):
    return Author.objects.create(**payload.dict(exclude_unset=True))


@router.get("/{id}/", response=AuthorOut)
def get_author(request, id: int):
    return get_object_or_404(Author, pk=id)


@router.put("/{id}/", response=AuthorOut)
def update_author(request, id: int, payload: AuthorIn):
    author = get_object_or_404(Author, pk=id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(author, attr, value)
    author.save()
    return author


@router.delete("/{id}/", response={204: None})
def delete_author(request, id: int):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return 204, None
