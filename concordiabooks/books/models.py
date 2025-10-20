from django.db import models

class Textbook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    edition = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"
