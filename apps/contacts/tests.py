from django.test import TestCase

from apps.contacts.models import Contact


class InfoModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name='Abu',
            last_name='Sayem',
            date_of_birth='1993-10-25',
            contacts='+8801750721112',
            email='abusaayem@gmail.com',
            jabber='abusayem.42cc.co',
            skype='abusaayem',
            bio='This is sample bio',
            other_contacts='other contact info',
        )

    def test_string_representation(self):
        """Test string representaions of info model"""
        expected_info = f'{self.contact.name} {self.contact.last_name}'
        self.assertEqual(expected_info, str(self.contact))

    def test_info_exists(self):
        """Cheeck existing data of info model after insertion"""
        self.assertNotEqual(Contact.objects.count(), 0)


class ContactViewTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name='Abu',
            last_name='Sayem',
            date_of_birth='1993-10-25',
            contacts='+8801750721112',
            email='abusaayem@gmail.com',
            jabber='abusayem.42cc.co',
            skype='abusaayem',
            bio='This is sample bio',
            other_contacts='other contact info',
        )
        self.response = self.client.get('/')

    def test_can_visit_homepage(self):
        """  test can visit home page"""
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        """ test correct template is used """
        self.assertTemplateUsed(self.response, 'contacts/contact.html')
        self.assertTemplateUsed(self.response, 'base.html')
