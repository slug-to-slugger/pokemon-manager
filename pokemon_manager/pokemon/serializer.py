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
