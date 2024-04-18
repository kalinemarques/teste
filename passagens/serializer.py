from rest_framework import serializers
from passagens.models import *

class PassagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passagem
        fields ='__all__'

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passagem
        fields ='__all__'