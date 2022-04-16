import random
from locust import HttpUser, task, between


class ServiceUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://igih3eivbr.us-east-1.awsapprunner.com"

    @task
    def predict_post(self):
        self.client.post(
            "/predict",
            {
                "BMI": round(random.uniform(15, 35), 2),
                "Smoking": random.randint(0, 1),
                "AlcoholDrinking": random.randint(0, 1),
                "Stroke": random.randint(0, 1),
                "PhysicalHealth": random.randint(0, 1),
                "MentalHealth": random.randint(0, 1),
                "DiffWalking": random.randint(0, 1),
                "Sex": random.randint(0, 1),
                "AgeCategory": random.randint(0, 12),
                "Diabetic": random.randint(0, 1),
                "PhysicalActivity": random.randint(0, 1),
                "GenHealth": random.randint(0, 4),
                "SleepTime": random.randint(1, 12),
                "Asthma": random.randint(0, 1),
                "KidneyDisease": random.randint(0, 1),
                "SkinCancer": random.randint(0, 1),
            },
        )
