from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def view_site_info(self):
        self.client.get("/site-info/") 
    @task(1)
    def subscribe_to_newsletter(self):
        self.client.post("/newsletter/", {"email": "test@example.com"})
