from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """
    Extends the default User model with an additional color attribute.
    
    Attributes:
        user (OneToOneField): Links to the Django User model.
        color (CharField): Stores a color preference in HEX format.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.user.username