from rest_framework.serializers import ModelSerializer
from base.models import Reserva, Contato

class ReservaSerializer(ModelSerializer):
     class Meta:
          model = Reserva
          fields = ["id", "nome_do_pet", "telefone" , "data", "mensagem"]

class ContatoSerializer(ModelSerializer):
     class Meta:
          model = Contato
          fields = ["id", "nome", "email", "mensagem"]