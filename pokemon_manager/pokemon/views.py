from pokemon.models import Trainer, Pokemon
from pokemon.serializer import TrainerSerializer, PokemonSerializer
from rest_framework import generics
import logging

class TrainerList(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    # putメソッドをオーバーライド
    def put(self, request, *args, **kwargs):
        # request.dataの中身をログに出力
        logger = logging.getLogger('development')
        logger.info(request.data)
        return self.update(request, *args, **kwargs)

class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    # putメソッドをオーバーライド
    def put(self, request, *args, **kwargs):
        # request.dataの中身をログに出力
        logger = logging.getLogger('development')
        logger.info(request.data)
        return self.update(request, *args, **kwargs)