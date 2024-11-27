from django.test import TestCase, Client
from django.urls import reverse
from .models import Categorie, Publication

class FunctionalTests(TestCase):
    def setUp(self):
        # Initialisation du client
        self.client = Client()

        # Création des données
        self.categorie = Categorie.objects.create(
            nom="Catégorie Test",
            description="Description de la catégorie test",
        )
        self.publication = Publication.objects.create(
            titre="Publication Test",
            description="<p>Description test</p>",
            image="path/to/image.jpg",
            categorie=self.categorie,
        )

    def test_index_page_status_code(self):
        """Vérifie que la page d'accueil retourne un statut 200."""
        response = self.client.get(reverse("index"))  # Remplacez "index" par le nom de votre URL
        self.assertEqual(response.status_code, 200)

    def test_categorie_list_view(self):
        """Vérifie que la liste des catégories est accessible."""
        response = self.client.get(reverse("categories"))  # Nom de l'URL pour lister les catégories
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.categorie.nom)

    def test_publication_detail_view(self):
        """Vérifie que la page de détail d'une publication est accessible."""
        response = self.client.get(reverse("publication_detail", args=[self.publication.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.publication.titre)

    def test_publication_creation(self):
        """Vérifie la création d'une publication via une vue."""
        response = self.client.post(reverse("publication_create"), {
            "titre": "Nouvelle Publication",
            "description": "<p>Description de test</p>",
            "image": "path/to/new_image.jpg",
            "categorie": self.categorie.id,
        })
        self.assertEqual(response.status_code, 302)  # Redirection après création
        self.assertTrue(Publication.objects.filter(titre="Nouvelle Publication").exists())

    def test_publication_update(self):
        """Vérifie la mise à jour d'une publication existante."""
        response = self.client.post(reverse("publication_update", args=[self.publication.slug]), {
            "titre": "Publication Mise à Jour",
            "description": "<p>Description mise à jour</p>",
            "image": "path/to/updated_image.jpg",
            "categorie": self.categorie.id,
        })
        self.assertEqual(response.status_code, 302)  # Redirection après mise à jour
        self.publication.refresh_from_db()
        self.assertEqual(self.publication.titre, "Publication Mise à Jour")

    def test_publication_delete(self):
        """Vérifie la suppression d'une publication."""
        response = self.client.post(reverse("publication_delete", args=[self.publication.slug]))
        self.assertEqual(response.status_code, 302)  # Redirection après suppression
        self.assertFalse(Publication.objects.filter(id=self.publication.id).exists())
