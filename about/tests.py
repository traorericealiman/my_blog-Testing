from django.test import TestCase
from .models import Curriculum, Contact, Prestation, Presentation, Gallerie
from datetime import datetime

class CurriculumModelTest(TestCase):
    def setUp(self):
        self.curriculum = Curriculum.objects.create(
            photo='images/curriculum/test_image.jpg',
            nom='Test Curriculum',
            description='<p>This is a test description.</p>',
            cv='cv/curriculum/test_cv.pdf'
        )

    def test_curriculum_creation(self):
        self.assertEqual(self.curriculum.nom, 'Test Curriculum')
        self.assertTrue(self.curriculum.status)

    def test_str_representation(self):
        self.assertEqual(str(self.curriculum), 'Test Curriculum')


class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            nom='John Doe',
            email='johndoe@example.com',
            subject='Test Subject',
            telephone=1234567890,
            message='This is a test message.'
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.nom, 'John Doe')
        self.assertEqual(self.contact.email, 'johndoe@example.com')
        self.assertTrue(self.contact.status)

    def test_str_representation(self):
        self.assertEqual(str(self.contact), 'John Doe')


class PrestationModelTest(TestCase):
    def setUp(self):
        self.prestation = Prestation.objects.create(
            titre='Test Prestation',
            description='This is a test prestation.',
            image='images/prestations/test_image.jpg'
        )

    def test_prestation_creation(self):
        self.assertEqual(self.prestation.titre, 'Test Prestation')
        self.assertTrue(self.prestation.status)

    def test_str_representation(self):
        self.assertEqual(str(self.prestation), 'Test Prestation')


class PresentationModelTest(TestCase):
    def setUp(self):
        self.presentation = Presentation.objects.create(
            titre='Test Presentation',
            image='image/presentation/test_image.jpg',
            description='<p>This is a test presentation description.</p>'
        )

    def test_presentation_creation(self):
        self.assertEqual(self.presentation.titre, 'Test Presentation')
        self.assertTrue(self.presentation.status)

    def test_str_representation(self):
        self.assertEqual(str(self.presentation), 'Test Presentation')


class GallerieModelTest(TestCase):
    def setUp(self):
        self.gallerie = Gallerie.objects.create(
            gallerie='gallerie/image/test_image.jpg',
            titre='Test Gallerie'
        )

    def test_gallerie_creation(self):
        self.assertEqual(self.gallerie.titre, 'Test Gallerie')
        self.assertTrue(self.gallerie.status)

    def test_str_representation(self):
        self.assertEqual(str(self.gallerie), 'Test Gallerie')
