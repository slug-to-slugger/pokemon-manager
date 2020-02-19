from rest_framework import serializers
from pokemon.models import Trainer

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id','created','name','password','user_id']