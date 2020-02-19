from rest_framework import serializer

class TrainerSerializer(serializer.ModelSerializer):
    class Meta:
        model = Trainer
        field = ['id','created','name','password','user_id']