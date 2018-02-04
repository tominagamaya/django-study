from django.test import TestCase
from cms.models import Book
from cms.tests import create_book


class ViewTest(TestCase):

    def test_default_models(self):
        saved_book = Book.objects.all()
        self.assertEquals(saved_book.count(), 0)

    def test_one_models(self):
        book = Book()
        book.save()
        saved_books = Book.objects.all()
        self.assertEquals(saved_books.count(), 1)

    def test_book_create(self):
        book = create_book(self)
        self.assertTrue(isinstance(book, Book))
        self.assertEquals(book.__str__(), book.name)
