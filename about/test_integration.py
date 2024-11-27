from django.test import TestCase, Client
from models import Curriculum, Contact, Prestation, Presentation, Gallerie
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class IntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_image = SimpleUploadedFile(
            "test_image.jpg", content=b"file_content", content_type="image/jpeg"
        )
        self.test_pdf = SimpleUploadedFile(
            "test_cv.pdf", content=b"%PDF-1.4 test content", content_type="application/pdf"
        )

        self.curriculum = Curriculum.objects.create(
            photo=self.test_image,
            nom="Test Curriculum",
            description="<p>Description test</p>",
            cv=self.test_pdf
        )

    def test_curriculum_list_view(self):
        response = self.client.get(reverse('curriculum_list'))  # Assurez-vous que cette vue existe
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Curriculum")

    def test_contact_creation(self):
        data = {
            "nom": "John Doe",
            "email": "john.doe@example.com",
            "subject": "Test Subject",
            "telephone": 123456789,
            "message": "Test message"
        }
        response = self.client.post(reverse('contact_create'), data)
        self.assertEqual(response.status_code, 200)  # Ou 302 si redirection
        self.assertTrue(Contact.objects.filter(nom="John Doe").exists())
