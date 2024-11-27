from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase

class PoesieFunctionalTests(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Assurez-vous que ChromeDriver est installé

    def tearDown(self):
        self.browser.quit()

    def test_create_poesie(self):
        self.browser.get(f"{self.live_server_url}/admin/")  # Connectez-vous au panneau admin
        # Ajouter les étapes pour se connecter
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("admin")  # Remplacez par vos identifiants
        password_input.send_keys("admin")
        self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Naviguer et créer une nouvelle poésie
        self.browser.get(f"{self.live_server_url}/admin/app_name/poesie/add/")
        self.browser.find_element(By.NAME, "titre").send_keys("Poème Test")
        self.browser.find_element(By.NAME, "description").send_keys("Une poésie magnifique.")
        self.browser.find_element(By.NAME, "poeme").send_keys("<p>Voici une poésie d'exemple.</p>")
        self.browser.find_element(By.NAME, "_save").click()

        # Vérifier si la poésie est bien enregistrée
        self.browser.get(f"{self.live_server_url}/poesie/")
        self.assertIn("Poème Test", self.browser.page_source)
