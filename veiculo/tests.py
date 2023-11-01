from django.contrib.auth.models import User
from django.test import TestCase, client
from django.urls import reverse
from datetime import datetime
from veiculo.models import *
from veiculo.forms import *


class TestesModelVeiculo(TestCase):
    '''
    Classe de testes para model Veiculo.
    '''
    # EStrutura inicial do BD cria um novo BD temporario.
    def setUp(self):
        self.instancia = Veiculo(
            marca=1, 
            modelo='ABCDE',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )
    
    def test_is_new(self):
        self.assertTrue(self.instancia.veiculo_novo)
        self.instancia.ano = datetime.now().year - 5
        self.assertFalse(self.instancia.veiculo_novo)
    
    def test_years_use(self):
        self.instancia.ano = datetime.now().year - 10
        self.assertEqual(self.instancia.ano_de_uso(), 10)

class TestesViewListarVeiculos(TestCase):
    '''
    classe de testes para view ListarVeiculo
    '''

    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345@teste')
        self.client.force_login(self.user)
        self.url = reverse('listar-veiculos')
        Veiculo(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=4).save()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('veiculos')), 1)

class TestesViewCriarVeiculo(TestCase):
    '''
    classe de testes para view CriarVeiculo
    '''

    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345@teste')
        self.client.force_login(self.user)
        self.url = reverse('criar-veiculo')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)

    def test_post(self):
        data = {'marca': 1, 'modelo': 'ABCDE', 'ano': 2, 'cor': 3, 'combustivel': 2}
        response = self.client.post(self.url, data)

        #verificar se apos a inserção houve um redirecionamento para a view ListarVeiculos
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))

        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'ABCDE')

class TestesViewEditarVeiculo(TestCase):
    '''
    classe de testes para view EditarVeiculo
    '''

    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345@teste')
        self.client.force_login(self.user)
        self.instancia = Veiculo.objects.create(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=4)
        self.url = reverse('editar-veiculo', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)
        self.assertEqual(response.context.get('object').marca, 1)


    def test_post(self):
        data = {'marca': 5, 'modelo': 'ABCDE', 'ano': 4, 'cor': 2, 'combustivel': 2}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 5)
        self.assertEqual(Veiculo.objects.first().pk, self.instancia.pk)

class TestesViewDeletarVeiculo(TestCase):
    '''
    classe de testes para view DeletarVeiculo
    '''

    def setUp(self):
        self.user = User.objects.create(username='teste', password='12345@teste')
        self.client.force_login(self.user)
        self.instancia = Veiculo.objects.create(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=4)
        self.url = reverse('deletar-veiculo', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)

    def test_post(self):
        response = self.client.post(self.url)

        #verifica se apos a exclusão houve um redirecionamento para view ListarVeiculos
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)