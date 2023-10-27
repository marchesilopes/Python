# API IBGE
# HTTPS://servicodados.ibge.gov.br/docs
import requests
import pandas as pd

link_P = "https://servicodados.ibge.gov.br/api/v3/agregados/4714/periodos/2022/variaveis/93?localidades=N6[4314902]"
link_D = "https://servicodados.ibge.gov.br/api/v3/agregados/4711/periodos/2022/variaveis/617?localidades=N6[4314902]&classificacao=3[59993]"

requisicao_P = requests.get(link_P)
informacoes_P = requisicao_P.json()

requisicao_D = requests.get(link_D)
informacoes_D = requisicao_D.json()

item_busca_P = informacoes_P[0]['resultados'][0]['series'][0]['localidade']['nome']
Populacao = int(informacoes_P[0]['resultados'][0]['series'][0]['serie']['2022'])

item_busca_D = informacoes_D[0]['resultados'][0]['series'][0]['localidade']['nome']
Domicilios = int(informacoes_D[0]['resultados'][0]['series'][0]['serie']['2022'])

print(f'O valor total da população de Porto Alegre é {Populacao:,}.')
print(f'O número total de domicílios em Porto Alegre é de {Domicilios:,}')
