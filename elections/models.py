# models.py

from django.db import models
from django.contrib.auth.models import User

class Election(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing'), ('completed', 'Completed')])

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='candidates/', null=True, blank=True)
    description = models.TextField()
    election = models.ForeignKey(Election, on_delete=models.CASCADE, default=1)

    def total_votes(self):
        return Vote.objects.filter(candidate=self).count()

    def __str__(self):
        return f"{self.name} - Total Votes: {self.total_votes()}"

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    block_hash = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"Vote for {self.candidate.name} by {self.user.username}"
