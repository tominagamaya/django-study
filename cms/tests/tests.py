from django.core.urlresolvers import reverse
from django.test import TestCase

from cms.forms import BookForm
from cms.models import Book


class ViewTest(TestCase):

    # Modelsのテスト
    def test_default_models(self):
        saved_book = Book.objects.all()
        self.assertEquals(saved_book.count(), 0)

    def test_one_models(self):
        book = Book()
        book.save()
        saved_books = Book.objects.all()
        self.assertEquals(saved_books.count(), 1)

    def create_book(self, name="はじめてのDjango", publisher="d jango", page="50"):
        return Book.objects.create(name=name, publisher=publisher, page=page)

    def test_book_create(self):
        book = self.create_book()
        self.assertTrue(isinstance(book, Book))
        self.assertEquals(book.__str__(), book.name)

    # Viewsのテスト
    def test_book_list_view(self):
        book = self.create_book()
        url = reverse('cms:book_list')
        resp = self.client.get(url)

        self.assertEquals(resp.status_code, 200)
        self.assertIn(book.name, bytes(resp.content).decode('utf-8'))

    # Formのテスト
    def test_valid_form(self):
        book = Book.objects.create(name='Django Book', publisher='d jan go', page='100')
        data = {'name': book.name, 'publisher': book.publisher, 'page': book.page, }
        form = BookForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        book = Book.objects.create(name='', publisher='', page='0')
        data = {'name': book.name, 'publisher': book.publisher, 'page': book.page, }
        form = BookForm(data=data)
        self.assertFalse(form.is_valid())
