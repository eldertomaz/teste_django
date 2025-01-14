from django.test import TestCase
from django.contrib.auth.models import User
from core.apps.base.models import set_current_user
from core.apps.user import models

class TestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="12345")
        set_current_user(self.user)


    def test_tenant_set_on_save(self):
        programmers = models.Programmers.objects.create(title="Teste", content="Conteúdo de teste")
        self.assertEqual(programmers.tenant, self.user)