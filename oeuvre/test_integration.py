from django.test import TestCase, Client
from .models import Poesie
from django.urls import reverse
from tinymce.models import HTMLField

class PoesieIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.poesie = Poesie.objects.create(
            titre="La Beauté du Crépuscule",
            description="Un poème sur la beauté du soir.",
            poeme="<p>Au crépuscule, la lumière danse sur les vagues...</p>",
        )

    def test_poesie_list_view(self):
        response = self.client.get(reverse('poesie_list'))  # Adaptez le nom de la vue si nécessaire
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "La Beauté du Crépuscule")

    def test_poesie_detail_view(self):
        response = self.client.get(reverse('poesie_detail', args=[self.poesie.id]))  # Assurez-vous que cette vue existe
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<p>Au crépuscule, la lumière danse sur les vagues...</p>")
