from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def show_summary(self):
        self.client.post("/showSummary",
                         {"email": "admin@irontemple.com"})

    @task
    def purchase_places(self):
        self.client.post("/purchasePlaces",
                         {"competition": "Fall Classic",
                          "club": "She Lifts",
                          "places": "1"
                          })

    @task
    def points_display(self):
        self.client.get("/showClubsPoints")

    @task
    def logout(self):
        self.client.get("/logout")