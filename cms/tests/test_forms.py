from django.test import TestCase
from cms.forms import BookForm
from cms.models import Book


class ViewTest(TestCase):

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
