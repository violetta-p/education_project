from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


from education.models import Module
from users.models import User

current_date = date.today().strftime("%Y-%m-%d")


class ModuleTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create(
            email="Test@mail.ru",
            password="Test12345",
            is_active=True,
        )
        cls.module = Module.objects.create(
            ordinal=1,
            name='test_module',
            description='It is a test-module',
            user=cls.user
        )

    def test_get_name(self):
        test_module = Module.objects.get(pk=1)
        self.assertEqual(str(test_module), test_module.name)

    def test_get_list(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)

        response = self.client.get(
            reverse('education:module_list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{
                "id": 1,
                "ordinal": 1,
                "name": 'test_module',
                "description": 'It is a test-module',
                "creation_date": current_date,
                "user": self.user.id
            }]
        )

    def test_create_module(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)

        data = {
            'ordinal': 2,
            'name': 'test_module',
            'description': 'It is the second test-module',
        }

        response = self.client.post(
            reverse('education:module_create'),
            data=data

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_module(self):
        data2 = {
            'ordinal': 2,
            'name': 'test_updated',
            'description': 'It is the second test-module',
        }
        response = self.client.put(
            reverse('education:module_update', kwargs={'pk': self.module.pk}),
            data=data2,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_module(self):
        response = self.client.delete(
            reverse('education:module_delete', kwargs={'pk': self.module.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
