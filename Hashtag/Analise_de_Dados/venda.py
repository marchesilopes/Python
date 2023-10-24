# INTRODUÇÃO A ANÁLISE DE DADOS
# Como funciona um Projeto de Análise de DAdos?
# Os projetos de Análise de dados são na verdade Desafios das Empresas

# DESAFIO
# - Empresa vende bermudas
# - 5 Lojas
# - Está querendo aumentar as vendas
# O que fazer?
# Informações Disponíveis: Base de Vendas

# Passo 1 - Trazer sua base de dados para o Python e ver o que tem nela
import pandas as pd

tabela = pd.read_excel("C:/Users/gabriel.marchesi/Desktop/Estatística/Python/pythonProject/GitHub/Python/Hashtag/Analise_de_Dados/Vendas.xlsx")
print(tabela)

# Passo 2 - Pegar um panorama geral sobre a sua base de dados
faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)

# Passo 3 - Começar sua análise Top->Down
# faturamento por loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)

# Passo 4 - Entrar no detalhe para entender
faturamento_por_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
print(faturamento_por_produto)