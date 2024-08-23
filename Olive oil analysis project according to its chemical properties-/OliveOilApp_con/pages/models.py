from django.db import models
from django.contrib.auth.models import User

class OliveOil(models.Model):
    OIL_TYPES = [
        ('EVOO', 'Extra Virgin Olive Oil (EVOO)'),
        ('VOO', 'Virgin Olive Oil (VOO)'),
        ('ROO', 'Refined Olive Oil (ROO)'),
        ('OO', 'Olive Oil (OO)'),
    ]

    name = models.CharField(max_length=100)
    oil_type = models.CharField(max_length=4, choices=OIL_TYPES)
    acidity = models.FloatField()  # Acidity percentage
    peroxide_value = models.FloatField()  # Peroxide value
    k232 = models.FloatField()  # K232 value
    k270 = models.FloatField()  # K270 value
    delta_k = models.FloatField()  # Delta-K value
    total_polyphenols = models.FloatField()  # Total polyphenols (mg/kg)
    moisture_and_volatiles = models.FloatField()  # Moisture and volatile matter percentage
    pyropheophytins = models.FloatField()  # Pyropheophytins percentage
    dag_content = models.FloatField()  # 1,2-Diacylglycerol content percentage
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='olive_oils')

    def calculate_quality_score(self):
        # Define weights
        weights = {
            'acidity': 0.15,
            'peroxide_value': 0.10,
            'k232': 0.10,
            'k270': 0.10,
            'delta_k': 0.05,
            'total_polyphenols': 0.15,
            'moisture_and_volatiles': 0.05,
            'pyropheophytins': 0.10,
            'dag_content': 0.20,
        }

        # Get scores based on values
        scores = {
            'acidity': self.get_acidity_score(),
            'peroxide_value': self.get_peroxide_value_score(),
            'k232': self.get_k232_score(),
            'k270': self.get_k270_score(),
            'delta_k': self.get_delta_k_score(),
            'total_polyphenols': self.get_total_polyphenols_score(),
            'moisture_and_volatiles': self.get_moisture_and_volatiles_score(),
            'pyropheophytins': self.get_pyropheophytins_score(),
            'dag_content': self.get_dag_content_score(),
        }

        # Calculate total quality score
        total_score = sum(weights[param] * scores[param] for param in weights)
        return round(total_score, 2)

    def get_acidity_score(self):
        if self.acidity <= 0.3:
            return 10
        elif self.acidity <= 0.8:
            return 7.5
        elif self.acidity <= 1.5:
            return 5
        else:
            return 2.5

    def get_peroxide_value_score(self):
        if self.peroxide_value <= 10:
            return 10
        elif self.peroxide_value <= 15:
            return 7.5
        elif self.peroxide_value <= 20:
            return 5
        else:
            return 2.5

    def get_k232_score(self):
        if self.k232 <= 2.0:
            return 10
        elif self.k232 <= 2.5:
            return 7.5
        elif self.k232 <= 2.6:
            return 5
        else:
            return 2.5

    def get_k270_score(self):
        if self.k270 <= 0.2:
            return 10
        elif self.k270 <= 0.25:
            return 7.5
        elif self.k270 <= 0.3:
            return 5
        else:
            return 2.5

    def get_delta_k_score(self):
        if self.delta_k <= 0.01:
            return 10
        elif self.delta_k <= 0.02:
            return 7.5
        elif self.delta_k <= 0.03:
            return 5
        else:
            return 2.5

    def get_total_polyphenols_score(self):
        if self.total_polyphenols > 400:
            return 10
        elif self.total_polyphenols >= 300:
            return 7.5
        elif self.total_polyphenols >= 200:
            return 5
        else:
            return 2.5

    def get_moisture_and_volatiles_score(self):
        if self.moisture_and_volatiles <= 0.1:
            return 10
        elif self.moisture_and_volatiles <= 0.2:
            return 7.5
        elif self.moisture_and_volatiles <= 0.3:
            return 5
        else:
            return 2.5

    def get_pyropheophytins_score(self):
        if self.pyropheophytins <= 10:
            return 10
        elif self.pyropheophytins <= 15:
            return 7.5
        elif self.pyropheophytins <= 20:
            return 5
        else:
            return 2.5

    def get_dag_content_score(self):
        if self.dag_content >= 90:
            return 10
        elif self.dag_content >= 80:
            return 7.5
        elif self.dag_content >= 70:
            return 5
        else:
            return 2.5

    def __str__(self):
        return self.name
