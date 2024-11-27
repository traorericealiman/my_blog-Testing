from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class FunctionalTests(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Assurez-vous que ChromeDriver est installé

    def tearDown(self):
        self.browser.quit()

    def test_contact_form_submission(self):
        self.browser.get(f"{self.live_server_url}/contact/")
        self.browser.find_element(By.NAME, "nom").send_keys("John Doe")
        self.browser.find_element(By.NAME, "email").send_keys("john.doe@example.com")
        self.browser.find_element(By.NAME, "subject").send_keys("Test Subject")
        self.browser.find_element(By.NAME, "telephone").send_keys("123456789")
        self.browser.find_element(By.NAME, "message").send_keys("Test Message")
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Vérifiez que la page montre un message de succès
        success_message = self.browser.find_element(By.CLASS_NAME, "success").text
        self.assertIn("Votre message a été envoyé", success_message)
