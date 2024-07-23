from rest_framework import serializers
from .models import Question

class Bot_app(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')

