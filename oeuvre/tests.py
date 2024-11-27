from django.test import TestCase
from .models import Poesie

class PoesieModelTest(TestCase):
    def setUp(self):
        # Création d'une instance de Poesie pour les tests
        self.poesie = Poesie.objects.create(
            titre='La Nuit Étoilée',
            description='Un poème sur la beauté de la nuit.',
            poeme='<p>Les étoiles dansent dans le ciel obscur...</p>',
        )

    def test_poesie_creation(self):
        """Test pour vérifier que l'instance est bien créée avec les valeurs attendues."""
        self.assertEqual(self.poesie.titre, 'La Nuit Étoilée')
        self.assertEqual(self.poesie.description, 'Un poème sur la beauté de la nuit.')
        self.assertIn('<p>Les étoiles dansent', self.poesie.poeme)
        self.assertTrue(self.poesie.status)

    def test_date_fields_auto_generated(self):
        """Test pour vérifier que les champs de date sont correctement remplis."""
        self.assertIsNotNone(self.poesie.date_add)
        self.assertIsNotNone(self.poesie.date_update)

    def test_str_representation(self):
        """Test pour vérifier que la méthode __str__ retourne le titre."""
        self.assertEqual(str(self.poesie), 'La Nuit Étoilée')
