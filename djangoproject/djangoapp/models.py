from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Define your models here.

class ChaiVarity(models.Model):
    # Define chai type choices
    chai_type_choice = [
        ('ml', 'masala'),
        ('gr', 'ginger'),
    ]
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='djangoimage/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=chai_type_choice)

    def __str__(self):
        return self.name

# One-to-many relationship
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'

# Many-to-many relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name

# One-to-one relationship
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'
