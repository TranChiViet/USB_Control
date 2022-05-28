from rest_framework.serializers import ModelSerializer
from .models import GamePad

class GamePadSerializer(ModelSerializer):
    class Meta:
        model = GamePad
        fields = '__all__'