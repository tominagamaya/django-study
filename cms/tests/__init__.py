from cms.models import Book


def create_book(self, name="はじめてのDjango", publisher="d jango", page="50"):
    return Book.objects.create(name=name, publisher=publisher, page=page)

