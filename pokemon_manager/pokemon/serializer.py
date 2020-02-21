from rest_framework import serializers
from pokemon.models import Trainer, Pokemon

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id','created','name','password','user_id']

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        # fields = ['name', 'special_skill', ]s
        fields = '__all__'