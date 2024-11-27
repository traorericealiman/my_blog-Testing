from django.test import TestCase
from django.utils.text import slugify
from datetime import datetime
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Evenement, Cours, Textes, Video

# Create your tests here.

#TestCategorie
class CategorieModelTest(TestCase):
    def setUp(self):
        #les données nécessaires pour le test.
        self.categorie = Categorie.objects.create(
            nom="Catégorie Test", 
            description="Description de test"
        )

    def test_categorie_creation(self):
        #Tester si la catégorie est bien créée 
        self.assertEqual(self.categorie.nom, "Catégorie Test")
        self.assertTrue(self.categorie.status)  
    
    def test_categorie_str(self):
        #Tester si le nom de la catégorie est envoyé
        self.assertEqual(str(self.categorie), "Catégorie Test")

#TestPublication
class PublicationModelTest(TestCase):
    def setUp(self):
        #Préparer une catégorie et une publication
        self.categorie = Categorie.objects.create(nom="Catégorie Test", description="Description")
        self.publication = Publication.objects.create(
            titre="Titre Test",
            description="Description Test",
            categorie=self.categorie,
            image="image/test.jpg"
        )

    def test_publication_creation(self):
        #Tester si la publication créée."""
        self.assertEqual(self.publication.titre, "Titre Test")
        self.assertTrue(self.publication.status)

    def test_publication_slug(self):
        #Tester si le slug est généré automatiquement 
        slug = '-'.join((slugify(self.publication.titre), slugify(datetime.now().microsecond)))
        self.assertTrue(slug.startswith(self.publication.slug))
    
    def test_publication_str(self):
        #Tester si le bon titre est envoyé
        self.assertEqual(str(self.publication), "Titre Test")

#TestCommentaire
class CommentaireTest(TestCase):
    def setUp(self):
        # Créer une catégorie valide pour la publication
        self.categorie = Categorie.objects.create(nom="Catégorie Test")
        
        # Créer une publication pour les tests de commentaires avec une catégorie
        self.publication = Publication.objects.create(
            titre="Publication pour tester les commentaires",
            description="Description de la publication",
            image="image/test.jpg",  # Si vous avez une image ou modifiez selon vos besoins
            categorie=self.categorie  # Assurez-vous de spécifier la catégorie
        )

    def test_commentaire_multiple_identique(self):
        # Créer un premier commentaire
        commentaire1 = Commentaire.objects.create(
            publication=self.publication,
            nom="Utilisateur 1",
            email="user1@example.com",
            commentaire="Premier commentaire"
        )

        # Créer un commentaire identique pour la même publication par le même utilisateur
        commentaire2 = Commentaire.objects.create(
            publication=self.publication,
            nom="Utilisateur 1",
            email="user1@example.com",
            commentaire="Premier commentaire"
        )

        # Vérifier qu'il y a bien deux commentaires dans la base de données
        self.assertEqual(Commentaire.objects.count(), 2)

        # Vérifier que les deux commentaires sont distincts
        self.assertNotEqual(commentaire1.id, commentaire2.id)

#TestReponseCommentaire
class ReponseCommentaireTest(TestCase):
    def setUp(self):
        # Créer une catégorie pour la publication
        self.categorie = Categorie.objects.create(nom="Catégorie Test")
        
        # Créer une publication pour les tests
        self.publication = Publication.objects.create(
            titre="Publication pour tester les commentaires et réponses",
            description="Description de la publication",
            image="image/test.jpg",  
            categorie=self.categorie 
        )

        # Créer un commentaire pour la publication
        self.commentaire = Commentaire.objects.create(
            publication=self.publication,
            nom="Utilisateur 1",
            email="user1@example.com",
            commentaire="Premier commentaire"
        )

    def test_repondre_au_commentaire(self):
        reponse1 = ReponseCommentaire.objects.create(
            commentaire=self.commentaire,
            nom="Utilisateur 2",
            email="user2@example.com",
            reponse="Réponse au premier commentaire"
        )

        # Vérifier que la réponse est bien enregistrée dans la base de données
        self.assertEqual(ReponseCommentaire.objects.count(), 1)

        # Vérifier que la réponse appartient bien au bon commentaire
        self.assertEqual(reponse1.commentaire, self.commentaire)

#TestEvent
class EvenementTest(TestCase):
    
    def setUp(self):
        self.evenement = Evenement.objects.create(
            titre="Conférence Django",
            description="<p>Description de l'événement</p>",
            image="evenemant/image/test_image.jpg"
        )
    
    def test_evenement_creation(self):
        self.assertEqual(self.evenement.titre, "Conférence Django")
        self.assertTrue(self.evenement.slug.startswith(slugify("Conférence Django")))
        self.assertEqual(self.evenement.description, "<p>Description de l'événement</p>")

    def test_slug_is_unique(self):
        evenement_2 = Evenement.objects.create(
            titre="Atelier Python",
            description="<p>Description de l'atelier</p>",
            image="evenemant/image/test_image2.jpg"
        )
        self.assertNotEqual(self.evenement.slug, evenement_2.slug)
   

#TestCours
class CoursTest(TestCase):
    
    def setUp(self):
        self.cours = Cours.objects.create(
            titre="Django pour les débutants",
            niveau="Débutant",
            annee=2024,
            description="Cours sur Django",
            image="cours/image/test_cours.jpg",
            cours="cours/cours/test_cours.pdf"
        )
    
    def test_cours_creation(self):
        self.assertEqual(self.cours.titre, "Django pour les débutants")
        self.assertEqual(self.cours.niveau, "Débutant")
        self.assertEqual(self.cours.annee, 2024)
        self.assertEqual(self.cours.description, "Cours sur Django")
        self.assertTrue(self.cours.image.url.startswith("/media/cours/image/test_cours.jpg"))
        self.assertTrue(self.cours.cours.url.startswith("/media/cours/cours/test_cours.pdf"))

#TestTextes

class TextesTest(TestCase):
    
    def setUp(self):
        self.texte = Textes.objects.create(
            titre="Introduction à Python",
            description="Un texte pour apprendre Python",
            image="textes/image/test_texte.jpg",
            pdf="pdf/textes/test_texte.pdf"
        )
    
    def test_textes_creation(self):
        self.assertEqual(self.texte.titre, "Introduction à Python")
        self.assertEqual(self.texte.description, "Un texte pour apprendre Python")
        self.assertTrue(self.texte.image.url.startswith("/media/textes/image/test_texte.jpg"))
        self.assertTrue(self.texte.pdf.url.startswith("/media/pdf/textes/test_texte.pdf"))

#TestVideo
class VideoTest(TestCase):
    
    def setUp(self):
        self.video = Video.objects.create(
            titre="Apprendre Django",
            description="Vidéo tutoriel Django",
            image="video/image/test_video.jpg",
            video="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )
    
    def test_video_creation(self):
        self.assertEqual(self.video.titre, "Apprendre Django")
        self.assertEqual(self.video.description, "Vidéo tutoriel Django")
        self.assertTrue(self.video.image.url.startswith("/media/video/image/test_video.jpg"))
        self.assertEqual(self.video.video, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        
    def test_get_video_method(self):
        # Test the property method that extracts the video ID from YouTube URL
        self.assertEqual(self.video.get_video, "dQw4w9WgXcQ")