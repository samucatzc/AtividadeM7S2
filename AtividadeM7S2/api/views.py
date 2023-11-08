from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from base.models import Reserva, Contato
from api.serializers import ReservaSerializer, ContatoSerializer

class ReservaViewSet(ModelViewSet):
     serializer_class = ReservaSerializer
     queryset = Reserva.objects.all()

class ContatoViewSet(ModelViewSet):
     serializer_class = ContatoSerializer
     queryset = Contato.objects.all()

@api_view()
def reservas(request):
     consulta = Reserva.objects.all()
     dados = []
     for reserva in consulta:
          dado = {
               "id": reserva.id,
               "nome_do_pet" : reserva.nome_do_pet,
               "telefone" : reserva.telefone,
               "data" : reserva.data,
               "mensagem" : reserva.mensagem
          }
          dados.append(dado)

     return Response(dados)

@api_view()
def contatos(request):
     consulta = Contato.objects.all()
     dados = []
     for contato in consulta:
          dado = {
               "id": contato.id,
               "nome" : contato.nome,
               "email" : contato.email,
               "mensagem" : contato.mensagem,
          }
          dados.append(dado)

     return Response(dados)