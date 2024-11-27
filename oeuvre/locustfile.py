from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def view_poesie_list(self):
        self.client.get("/poesie/")  # Endpoint pour la liste des poésies

    @task(1)
    def view_poesie_detail(self):
        self.client.get("/poesie/1/")  # Adaptez l'ID selon vos données
