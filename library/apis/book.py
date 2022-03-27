from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from library.models import Book
from library.schemas import BookOut

router = Router(tags=["book"])


@router.get("/", response=List[BookOut])
def list_books(request):
    return Book.objects.all()


@router.get("/{id}/", response=BookOut)
def get_book(request, id: int):
    return get_object_or_404(Book, pk=id)


@router.delete("/{id}/", response={204: None})
def delete_book(request, id: int):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return 204, None
