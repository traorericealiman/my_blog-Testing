from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(2)  # La tâche sera exécutée deux fois plus souvent que les autres
    def index(self):
        self.client.get("/")

    @task(1)
    def categories(self):
        self.client.get("/categories/")

    @task(1)
    def publication_detail(self):
        # Remplacez par un slug valide de votre base de données
        slug = "publication-test-123456"
        self.client.get(f"/publication/{slug}/")

    @task(1)
    def create_publication(self):
        # Exemple de données pour créer une publication
        data = {
            "titre": "Test Locust",
            "description": "<p>Test de description</p>",
            "image": "path/to/image.jpg",
            "categorie": 1,  # Assurez-vous que cette catégorie existe dans la base
        }
        self.client.post("/publication/create/", data)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Temps d'attente entre les requêtes (1 à 5 secondes)
