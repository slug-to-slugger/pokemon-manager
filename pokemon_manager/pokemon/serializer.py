import logging

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from pokemon.models import Trainer, Partner

logger = logging.getLogger('development')


class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = ('id', 'username', 'login_id', 'password', 'created')

    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data['password'] = make_password(password)
        return Trainer.objects.create(**validated_data)


class PartnerSerializer(serializers.ModelSerializer):
    pokemon = serializers.ReadOnlyField(source='pokemon.name')
    trainer = serializers.ReadOnlyField(source='trainer.username')

    class Meta:
        model = Partner
        fields = (
            'id', 'name', 'ability', 'character', 'gender',
            'h', 'a', 'b', 'c', 'd', 's', 'pokemon', 'trainer', 'updated_at'
        )

    def create(self, validated_data):
        return Partner.objects.create(**validated_data)
