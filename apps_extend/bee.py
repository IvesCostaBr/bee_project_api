import requests
import json

def cep(cep_input): #função cep vai me retornar o bairro
    if len(cep_input) != 8:
        print("Quantidade de digitos invalido!")
        exit()
            
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    adress_data = request.json()

    if 'erro' not in adress_data:
        bair = adress_data['bairro']
        bair = bair.lower()
        return bair

    else:
        print("CEP INVALIDO!")


def calcula_taxa(busca): #recebe o bairro da função de busca cep
    file = open('bairros.json', 'r')
    dados = json.load(file)
    file = cep(busca)
    for k,v in dados.items():
        if(k == file):
            vl = v
            print('Taxa de entrega ==> R$: {}'.format(vl))
            return vl

