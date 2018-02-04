from django.core.urlresolvers import reverse
from django.test import TestCase
from cms.tests import create_book


class ViewTest(TestCase):

    def test_book_list_view(self):
        book = create_book(self)
        url = reverse('cms:book_list')
        resp = self.client.get(url)

        self.assertEquals(resp.status_code, 200)
        self.assertIn(book.name, bytes(resp.content).decode('utf-8'))
