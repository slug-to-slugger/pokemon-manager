from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from pokemon.models import Trainer, Partner, Pokemon
from pokemon.serializer import TrainerSerializer, PartnerSerializer


class TrainerList(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainerDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class PartnerList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    def perform_create(self, serializer):
        return serializer.save(
            trainer=self.request.user,
            pokemon=Pokemon.objects.filter(guide_num=self.request.data.get('pokemon_id')).first()
        )


class PartnerDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
