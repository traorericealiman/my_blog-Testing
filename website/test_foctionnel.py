from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase

class NewsletterFunctionalTests(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_newsletter_subscription(self):
        self.browser.get(f"{self.live_server_url}/newsletter/")  # Remplacez par l'URL de votre vue
        email_input = self.browser.find_element(By.NAME, "email")
        email_input.send_keys("test@example.com")
        self.browser.find_element(By.NAME, "submit").click()

        # Vérifiez si un message de succès ou une redirection a eu lieu
        success_message = self.browser.find_element(By.ID, "success-message").text
        self.assertIn("Merci pour votre inscription", success_message)
