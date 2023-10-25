# Importação
import matplotlib.pyplot as plt

# plot()
#x = [1, 2, 3, 4]
#y = [2, 3, 4, 3]

# Gráfico de linhas
#plt.plot(x, y, label='dados', linestyle='dashed', color='g', lw='3.0')
#plt.ylabel('Eixo y')
#plt.xlabel('Eixo x')
#plt.title('Título do gráfico')
#plt.xticks([0, 2, 4, 6, 8, 9])
#plt.yticks([-1, 3, 5, 9, 11])
#plt.legend()

#Scatter plot
#plt.scatter(x, y, color='b', marker='s')

#Gráfico de barras
#plt.bar(x, y, color='k')

#plt.show()

# Subplots
#valoresx = [1, 2, 3, 4]
#valoresy = [1, 4, 2, 3]

#figura = plt.figure(figsize=(20,3))
#figura.suptitle('Título Geral')

#figura.add_subplot(131) #uma linha, 3 colunas e o gráfico é na posição 1
#plt.plot(valoresx, valoresy, label='Um dado qualquer')
#plt.legend()
#plt.title('Gráfico 1')

#figura.add_subplot(132) #uma linha, 3 colunas e o gráfico é na posição 2
#plt.scatter(valoresx, valoresy)
#plt.title('Gráfico 2')

#figura.add_subplot(133) #uma linha, 3 colunas e o gráfico é na posição 3
#plt.bar(valoresx, valoresy)
#plt.title('Gráfico 3')

#plt.savefig('gráficos.png')

#plt.show()

# APLICAÇÃO: Fonte de dados do Kaggle
import pandas as pd

cotacao_df = pd.read_csv('C:/Users/gabriel.marchesi/Desktop/Estatística/Python/pythonProject/GitHub/Python/Hashtag/Matplotlib/indexData.csv')
#print(cotacao_df)

cotacao_df1 = cotacao_df[['Index', 'Date', 'Close']]
df_remove = cotacao_df1.loc[(cotacao_df1['Index']!='NYA')]
cotacao_dffinal = cotacao_df1.drop(df_remove.index)
cotacao_dffinal = cotacao_dffinal[13900:]
print(cotacao_dffinal)
plt.figure(figsize=(10,4))
plt.plot(cotacao_dffinal['Date'], cotacao_dffinal['Close'], label='NYA', color='g', ls='--', lw='2')
plt.legend(loc=2, fontsize=18)
plt.ylabel('Valor do Fechamento')
plt.xlabel('Data da Cotação')
plt.title('Gráfico de cotação histórica da bolsa NYA')
#plt.axis(xmin='2021-03-01', xmax='2021-06-01')
plt.xticks(['2021-03-23', '2021-04-23', '2021-05-03'])

plt.show()