from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
    
class FriendshipPair(models.Model):
    user1 = models.ForeignKey(User, related_name='friend_1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='friend_2', on_delete=models.CASCADE)

    status = models.CharField(max_length=20, default='pending')  # pending, accepted, rejected
    is_confirmed = models.BooleanField(default=False)
    bond_level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"{self.user1.username} and {self.user2.username})"