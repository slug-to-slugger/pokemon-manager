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
        # 属性1が属性2より小さければ、逆にする
        if data.get('attribute1') > data.get('attribute2'):
            validated = {
                'attribute1': data.get('attribute2'),
                'attribute2': data.get('attribute1'),
            }
        else:
            validated = {}
        logging.warning(validated)
        return validated
