from rest_framework import serializers
from pokemon.models import Trainer, Partner
import logging
logger = logging.getLogger('development')


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'created', 'name', 'password', 'user_id']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

    def to_internal_value(self, data):
        validated = {}
        return validated
