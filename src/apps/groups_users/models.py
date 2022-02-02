from django.db import models


class UserGroups(models.Model):

    DATA_ANALYTICS = 'Data Analytics'
    SERVICES_ANALYTICS = 'Services Analytics'
    VOICE_ANALYTICS = 'Voice Analytics'
    QUEUE_STATS = 'Queue Stats'
    VOICE_STATS = 'Voice Stats'
    VIDEO = 'Video'
    SMART_ACCESS = 'Smart Access'
    DIAGRAMS = 'Diagrams'

    NAME_CHOICES = (
        (DATA_ANALYTICS, 'Data Analytics'),
        (SERVICES_ANALYTICS, 'Services Analytics'),
        (VOICE_ANALYTICS, 'Voice Analytics'),
        (QUEUE_STATS, 'Queue Stats'),
        (VOICE_STATS, 'Voice Stats'),
        (VIDEO, 'Video'),
        (SMART_ACCESS, 'Smart Access'),
        (DIAGRAMS, 'Diagrams')
    )

    name = models.CharField(
        "Name",
        max_length=100,
        choices=NAME_CHOICES,
        default=VIDEO
    )

    description = models.CharField(
        "Description",
        max_length=255
    )

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


