from rest_framework import serializers
from .models import Paragraph, Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['word']

class ParagraphSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'words', 'created_at', 'modified_at']