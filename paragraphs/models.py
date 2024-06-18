from django.db import models

class Paragraph(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50] + '...'

class Word(models.Model):
    word = models.CharField(max_length=255)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='words')

    def __str__(self):
        return self.word