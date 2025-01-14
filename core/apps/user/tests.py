from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from datetime import date, timedelta
from .models import Technologies, Programmers, Projects, Allocations



class BaseTest(TestCase):

    def setUp(self):
        # cria login
        self.user = User.objects.create_user(username='teste', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.user_2 = User.objects.create_user(username='batata', password='12345')

        # cria objetos base
        self.tech_1 = Technologies.objects.create(name='Python', tenant=self.user)
        self.tech_2 = Technologies.objects.create(name='Javascript', tenant=self.user)

        self.programmer = Programmers.objects.create(name='Dev_1', tenant=self.user)
        self.programmer.technologies.add(self.tech_1, self.tech_2)

        self.project = Projects.objects.create(
            name='Pro_1',
            start_date=date.today(),
            end_date=date.today() + timedelta(days=10),
            hours_day=8,
            tenant=self.user)
        self.project.technologies.add(self.tech_1)

        self.allocation = Allocations.objects.create(
            project=self.project,
            programmer=self.programmer,
            hours=4,
            tenant=self.user)
        

class CRUDTests(BaseTest):

    def crud_operations(self, model_name, data_create, data_update):
        url = f'/user/{model_name}/'

        # create
        response = self.client.post(url, data_create, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        resource_id = response.data['id']
        url_new = f'{url}{resource_id}/'

        # Read
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

        # Update
        response = self.client.patch(url_new, data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # access
        self.client.force_authenticate(user=self.user_2)
        response = self.client.get(url_new)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Delete
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url_new)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_technologies(self):
        self.crud_operations(
            model_name='technologies',
            data_create={"name": "Java"},
            data_update={"name": "Novo Java"}
        )

    def test_programmers(self):
        self.crud_operations(
            model_name='programmers',
            data_create={"name": "elder", "technologies": [self.tech_1.id, self.tech_2.id]},
            data_update={"name": "novo dev"}
        )

    def test_projects(self):
        self.crud_operations(
            model_name='projects',
            data_create={
                "name": "Projeto Django ",
                "start_date": date.today(),
                "end_date": date.today() + timedelta(days=5),
                "hours_day": 10,
                "technologies": [self.tech_1.id]
            },
            data_update={"name": "Django Verzel"}
        )

    def test_allocations(self):
        self.crud_operations(
            model_name='allocations',
            data_create={
                "project": self.project.id,
                "programmer": self.programmer.id,
                "hours": 5
            },
           data_update = {
                "project": self.project.id,
                "programmer": self.programmer.id,
                "hours": 7
            }
        )



class ValidationTests(BaseTest):

    #falha da validação de tecnologia
    def test_programmer_technology(self):
        self.programmer.technologies.clear()
        data = {
            "project": self.project.id,
            "programmer": self.programmer.id,
            "hours": 4
        }
        response = self.client.post('/user/allocations/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('O desenvolvedor deve possuir pelo menos uma tecnologia', str(response.data))


    #falha das datas do projeto inicio maior que final
    def test_project_date(self):
        data = {
            "name": "Invalid Proj",
            "start_date": date.today() + timedelta(days=10),
            "end_date": date.today(),
            "hours_day": 8,
            "technologies": [self.tech_1.id]
        }
        response = self.client.post('/user/projects/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("A data de início não pode ser maior que a data de finalização.", str(response.data))

    #falha das horas de desenvolvimento maior que a de projetos
    def test_allocation_hours(self):
        data = {
            "project": self.project.id,
            "programmer": self.programmer.id,
            "hours": 100
        }
        self.project.hours_day = 2
        self.project.save()

        response = self.client.post('/user/allocations/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("O total de horas alocadas não pode ultrapassar as horas planejadas para o projeto.", str(response.data))
