from django.test import TestCase
from django.urls import reverse
from main.models import PhonebookItem

class PhonebookTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_items = 13
        for item_num in range(number_of_items):
            PhonebookItem.objects.create(name='John %s' % item_num, phone_number='+19544442557',)
            
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/phonebookitem_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['page_obj']) == 10)

    def test_lists_second_page(self):
        resp = self.client.get(reverse('home')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['page_obj']) == 3)