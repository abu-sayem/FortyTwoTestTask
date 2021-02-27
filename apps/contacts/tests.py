from django.test import TestCase


class ContactViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_can_visit_homepage(self):
        """  test can visit home page"""
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        """ test correct template is used """
        self.assertTemplateUsed(self.response, 'contacts/contact.html')
        self.assertTemplateUsed(self.response, 'base.html')
