from django.test import TestCase
from .models import SiteInfo, SocialCount, Newsletter

class SiteInfoTest(TestCase):
    def setUp(self):
        self.site_info = SiteInfo.objects.create(
            email="contact@site.com",
            nom="Site Example",
            telephone=123456789,
            description="Description du site.",
            logo="logo/site/test_logo.jpg",
        )

    def test_siteinfo_creation(self):
        #Test si SiteInfo est correctement créé avec les valeurs fournies.
        self.assertEqual(self.site_info.email, "contact@site.com")
        self.assertEqual(self.site_info.nom, "Site Example")
        self.assertEqual(self.site_info.telephone, 123456789)
        self.assertEqual(self.site_info.description, "Description du site.")
        self.assertTrue(self.site_info.status)

    def test_string_representation(self):
        #Test si la méthode __str__ retourne le nom du site.
        self.assertEqual(str(self.site_info), "Site Example")


class SocialCountTest(TestCase):
    def setUp(self):
        self.social_count = SocialCount.objects.create(
            nom="Facebook",
            lien="https://www.facebook.com/example",
            icones="facebook",
        )

    def test_socialcount_creation(self):
        #Test si SocialCount est correctement créé avec les valeurs fournies.
        self.assertEqual(self.social_count.nom, "Facebook")
        self.assertEqual(self.social_count.lien, "https://www.facebook.com/example")
        self.assertEqual(self.social_count.icones, "facebook")
        self.assertTrue(self.social_count.status)

    def test_choices_validation(self):
        #Test si une valeur incorrecte dans le champ 'icones' lève une erreur.
        invalid_social_count = SocialCount(nom="Invalid", lien="https://invalid.com", icones="invalid_icon")
        with self.assertRaises(Exception):
            invalid_social_count.full_clean()

    def test_string_representation(self):
        """Test si la méthode __str__ retourne le nom."""
        self.assertEqual(str(self.social_count), "Facebook")


class NewsletterTest(TestCase):
    def setUp(self):
        self.newsletter = Newsletter.objects.create(
            email="user@example.com",
        )

    def test_newsletter_creation(self):
        """Test si Newsletter est correctement créée avec l'email fourni."""
        self.assertEqual(self.newsletter.email, "user@example.com")
        self.assertTrue(self.newsletter.status)

    def test_string_representation(self):
        """Test si la méthode __str__ retourne l'email."""
        self.assertEqual(str(self.newsletter), "user@example.com")
