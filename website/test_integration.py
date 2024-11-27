from django.test import TestCase
from .models import (
    Categorie, Publication, Commentaire, ReponseCommentaire, 
    Like, Evenement, Cours, Textes, Video
)

class ModelsIntegrationTest(TestCase):
    def setUp(self):
        # Création d'une catégorie
        self.categorie = Categorie.objects.create(
            nom="Catégorie Test",
            description="Description de la catégorie test",
        )

        # Création d'une publication liée à la catégorie
        self.publication = Publication.objects.create(
            titre="Titre de la publication",
            description="<p>Description en HTML</p>",
            image="path/to/image.jpg",
            categorie=self.categorie,
        )

        # Création d'un commentaire lié à la publication
        self.commentaire = Commentaire.objects.create(
            publication=self.publication,
            nom="Auteur du commentaire",
            email="auteur@example.com",
            commentaire="Ceci est un commentaire.",
        )

        # Création d'une réponse au commentaire
        self.reponse = ReponseCommentaire.objects.create(
            commentaire=self.commentaire,
            nom="Répondeur",
            email="repondeur@example.com",
            reponse="Ceci est une réponse au commentaire.",
        )

        # Création d'un like lié à la publication
        self.like = Like.objects.create(
            publication=self.publication
        )

        # Création d'un événement
        self.evenement = Evenement.objects.create(
            titre="Événement Test",
            description="<p>Description de l'événement</p>",
            image="path/to/event_image.jpg",
        )

        # Création d'un cours
        self.cours = Cours.objects.create(
            titre="Cours Test",
            niveau="Débutant",
            annee=2024,
            description="Description du cours",
            cours="path/to/cours.pdf",
        )

        # Création d'un texte
        self.texte = Textes.objects.create(
            titre="Texte Test",
            description="Description du texte",
            pdf="path/to/texte.pdf",
        )

        # Création d'une vidéo
        self.video = Video.objects.create(
            titre="Vidéo Test",
            description="Description de la vidéo",
            video="https://youtube.com/watch?v=example",
        )

    def test_categorie_publication_relation(self):
        """Vérifie que la relation entre Categorie et Publication fonctionne."""
        self.assertEqual(self.publication.categorie.nom, "Catégorie Test")

    def test_publication_commentaire_relation(self):
        """Vérifie que la relation entre Publication et Commentaire fonctionne."""
        self.assertEqual(self.commentaire.publication, self.publication)

    def test_commentaire_reponse_relation(self):
        """Vérifie que la relation entre Commentaire et ReponseCommentaire fonctionne."""
        self.assertEqual(self.reponse.commentaire, self.commentaire)

    def test_publication_like_relation(self):
        """Vérifie que le like est lié à la publication."""
        self.assertEqual(self.like.publication, self.publication)

    def test_evenement_creation(self):
        """Vérifie que l'événement est correctement créé."""
        self.assertEqual(self.evenement.titre, "Événement Test")

    def test_cours_creation(self):
        """Vérifie que le cours est correctement créé."""
        self.assertEqual(self.cours.titre, "Cours Test")

    def test_texte_creation(self):
        """Vérifie que le texte est correctement créé."""
        self.assertEqual(self.texte.titre, "Texte Test")

    def test_video_creation(self):
        """Vérifie que la vidéo est correctement créée."""
        self.assertEqual(self.video.titre, "Vidéo Test")

    def test_video_get_video_property(self):
        """Vérifie que la propriété `get_video` retourne l'ID YouTube."""
        self.assertEqual(self.video.get_video, "example")
