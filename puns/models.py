from django.db import models
from django.contrib.auth.models import User

class Pun(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]  # Display first 50 characters of the pun

class Rating(models.Model):
    pun = models.ForeignKey(Pun, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['pun', 'user'] 

    def __str__(self):
        return f'{self.pun} rated {self.rating} by {self.user}'
