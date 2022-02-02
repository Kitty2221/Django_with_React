from django.db import models


class User(models.Model):
    username = models.CharField(
        "Username",
        max_length=200,
        unique=True,
        null=False
    )

    group = models.ForeignKey(
        'groups_users.UserGroups',
        on_delete=models.PROTECT,
        null=False
    )

    created = models.DateField(
        "Created At",
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
