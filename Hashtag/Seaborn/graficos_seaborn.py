# Importação
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Importando a base de dados
df_videos = pd.read_excel('C:/Users/gabriel.marchesi/Desktop/Estatística/Python/pythonProject/GitHub/Python/Hashtag/Seaborn/videosYT.xlsx')
print(df_videos)

# Tipos de Gráficos
# Criando um gráfico de dispersão
#fig = sns.scatterplot(data=df_videos, x='Nº de Views', y='Nº de Likes', hue='Categoria', style='Responsável')
#plt.show()

# Criando um gráfico de dispersão (relacional)
#fig2 = sns.relplot(data=df_videos, x='Nº de Views', y='Nº de Likes', hue='Categoria', col='Responsável')
#fig2.set_titles('Responsável:{col_name}')
#plt.show()

# Criando um gráfico de linha
df_inscritos = pd.read_excel('C:/Users/gabriel.marchesi/Desktop/Estatística/Python/pythonProject/GitHub/Python/Hashtag/Seaborn/videosYT.xlsx', sheet_name='Inscritos')
print(df_inscritos)

#fig3 = sns.lineplot(data=df_inscritos, x='Mês/Ano', y='Inscritos', color='red')
#plt.show()

# Criando Histogramas
#fig4 = sns.displot(data=df_videos, x='Nº de Views', kind='hist', hue='Responsável')
#fig5 = sns.displot(data=df_videos, x='Nº de Views', kind='hist', hue='Responsável', col='Responsável')
#fig6 = sns.displot(data=df_videos, x='Nº de Views', kind='kde')
#fig7 = sns.displot(data=df_videos, x='Nº de Views', kind='ecdf')
#plt.show()

# Criando uma regressão linear
fig8 = sns.regplot(data=df_videos, x='Nº de Views', y='Nº de Likes')
fig9 = sns.lmplot(data=df_videos, x='Nº de Views', y='Nº de Likes', hue='Responsável')
fig10 = sns.lmplot(data=df_videos, x='Nº de Views', y='Nº de Likes', hue='Responsável', markers=['o','x'])
plt.show()