from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Temps entre chaque requête

    @task(2)
    def load_home_page(self):
        self.client.get("/")  # Endpoint pour la page d'accueil

    @task(1)
    def submit_contact_form(self):
        data = {
            "nom": "Test User",
            "email": "test@example.com",
            "subject": "Locust Test",
            "telephone": "123456789",
            "message": "This is a test message from Locust."
        }
        self.client.post("/contact/", data)
