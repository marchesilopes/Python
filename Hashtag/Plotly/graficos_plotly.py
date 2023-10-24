# Gráficos no Python - Plotly
# Importanto o Plotly
import plotly.express as px

# Criando um gráfico
dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]

# Gráfico de Linhas
fig = px.line(x = dados_x, y = dados_y, title='Vendas X Ano', width=600, height=300, line_shape='spline')
fig.update_yaxes(title='Vendas', title_font_color='#E8EB26')
#fig.show()

# Gráfico de Pizza
fig1 = px.pie(names=dados_x, values=dados_y, height=400, width=400)
fig1.update_traces(title_text='Pizza', title_position='top left')
#fig1.show()

# Gráfico de Barras
fig2 = px.bar(x=dados_x, y=dados_y, height=300, width=500)
#fig2.show()

# Gráfico de dispersão
dados1_x = [1, 4, 6, 7, 8, 4, 3, 2, 1, 5]
dados1_y = [10, 20, 5, 35, 2, 3, 40, 25, 16, 27]

fig3 = px.scatter(x = dados1_x, y = dados1_y, height=300, width=500)
#fig3.show()

# Caso de mercado de trabalho: Gráfico de Gantt
# Importando os dados
import pandas as pd

tarefas = pd.read_excel('C:/Users/gabriel.marchesi/Desktop/Estatística/Python/pythonProject/GitHub/Python/Hashtag/Plotly/Tarefas.xlsx')
print(tarefas)

fig4 = px.timeline(tarefas, x_start='Início', x_end='Fim', y='Tarefa')
fig4.update_yaxes(autorange='reversed')
fig4.show()

