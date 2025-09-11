# Importando as bibliotecas necessárias para o projeto
# pandas é excelente para trabalhar com DataFrames, que são como tabelas no Python
import pandas as pd
# matplotlib.pyplot é usado para criar gráficos e visualizações
import matplotlib.pyplot as plt
# seaborn é construído em cima do matplotlib e oferece gráficos estatísticos mais bonitos e fáceis de usar
import seaborn as sns
import numpy as np

# Carregando o conjunto de dados medical_examination.csv em um DataFrame do pandas
# O DataFrame será a nossa principal estrutura de dados para trabalhar com os dados médicos
df = pd.read_csv("medical_examination.csv")

# Vamos dar uma olhada nas primeiras linhas do nosso DataFrame para entender como os dados estão estruturados
print("Primeiras 5 linhas do DataFrame:")
print(df.head())

# Para ter uma visão geral das informações do DataFrame, como tipos de dados e valores não nulos
print("\nInformações gerais do DataFrame:")
df.info()

# Para obter estatísticas descritivas das colunas numéricas, como média, desvio padrão, etc.
print("\nEstatísticas descritivas do DataFrame:")
print(df.describe())

# Verificando se há valores nulos no DataFrame, o que é importante para a limpeza de dados
print("\nVerificando valores nulos no DataFrame:")
print(df.isnull().sum())

# --- Início da Fase 4: Implementação da análise de dados ---

# 1. Calcular o IMC (Índice de Massa Corporal) e adicionar a coluna \'overweight\'
# O IMC é calculado como peso (kg) / (altura (m))^2
# A altura está em cm, então precisamos converter para metros (dividir por 100)
# Criamos uma nova coluna \'overweight\' no DataFrame
# Se o IMC for > 25, a pessoa é considerada \'overweight\' (1), caso contrário (0)
df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)

# Vamos verificar as primeiras linhas novamente para ver a nova coluna
print("\nDataFrame com a nova coluna \'overweight\':")
print(df.head())

# 2. Normalizar os dados para as colunas \'cholesterol\' e \'gluc\'
# A instrução diz: Se o valor for 1, defina como 0. Se o valor for mais de 1, defina como 1.
# Isso significa que \'normal\' (1) vira 0 (bom) e \'acima do normal\' (2 ou 3) vira 1 (ruim).
# Usamos o np.where para aplicar essa lógica condicionalmente
df["cholesterol"] = np.where(df["cholesterol"] == 1, 0, 1)
df["gluc"] = np.where(df["gluc"] == 1, 0, 1)

# Vamos verificar as primeiras linhas novamente para ver as colunas normalizadas
print("\nDataFrame com \'cholesterol\' e \'gluc\' normalizados:")
print(df.head())


# 3. Função para desenhar o Gráfico Categórico (draw_cat_plot)
# Esta função criará um gráfico de barras que mostra a contagem de bons e maus resultados
# para as variáveis \'cholesterol\', \'gluc\', \'alco\', \'active\', \'smoke\' e \'overweight\'
# para pacientes com e sem doença cardiovascular (cardio=0 e cardio=1).
def draw_cat_plot():
    # Criar um DataFrame para o gráfico categórico usando pd.melt
    # Isso "derrete" o DataFrame, transformando colunas em linhas para facilitar a plotagem
    # id_vars são as colunas que queremos manter como identificadores
    # value_vars são as colunas que queremos "derreter"
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # Agrupar e reformatar os dados em df_cat para dividi-los por \'cardio\'
    # Contamos a ocorrência de cada \'value\' para cada \'variable\' e \'cardio\'
    # Usamos .size() para obter as contagens e .reset_index() para transformar o resultado em um DataFrame
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    # Criar o gráfico categórico usando seaborn.catplot()
    # kind="bar" indica que queremos um gráfico de barras
    # col="cardio" cria colunas separadas para cada valor de \'cardio\' (0 e 1)
    # x="variable" define as variáveis no eixo x
    # y="total" define as contagens no eixo y
    # hue="value" diferencia as barras por \'value\' (0 ou 1)
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar").fig

    # Retornar a figura
    return fig

# 4. Função para desenhar o Mapa de Calor (draw_heat_map)
# Esta função criará um mapa de calor da matriz de correlação dos dados
def draw_heat_map():
    # Limpar os dados em df_heat
    # Filtrar dados incorretos conforme as instruções:
    # - pressão diastólica (ap_lo) não pode ser maior que a sistólica (ap_hi)
    # - altura (height) deve estar entre o 2.5 e 97.5 percentil
    # - peso (weight) deve estar entre o 2.5 e 97.5 percentil
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calcular a matriz de correlação
    # O método .corr() calcula a correlação par a par de todas as colunas
    corr = df_heat.corr()

    # Gerar uma máscara para o triângulo superior
    # Isso é feito para evitar a duplicação de informações no mapa de calor
    # np.triu retorna a parte superior de um triângulo de uma matriz
    mask = np.triu(corr)

    # Configurar a figura do matplotlib
    # figsize define o tamanho da figura para melhor visualização
    fig, ax = plt.subplots(figsize=(12, 12))

    # Plotar o mapa de calor usando seaborn.heatmap()
    # annot=True para exibir os valores de correlação nas células
    # fmt=".1f" formata os valores para uma casa decimal
    # linewidths=0.5 adiciona linhas entre as células
    # ax=ax especifica o eixo onde o mapa de calor será plotado
    # mask=mask aplica a máscara para ocultar o triângulo superior
    # cbar_kws={'shrink': 0.5} ajusta o tamanho da barra de cores
    sns.heatmap(corr, annot=True, fmt=".1f", linewidths=0.5, ax=ax, mask=mask, cbar_kws={"shrink": 0.5})

    # Retornar a figura
    return fig

# Exemplo de como chamar as funções e salvar os gráficos (para teste)
# fig_cat = draw_cat_plot()
# fig_cat.savefig("catplot.png")

# fig_heat = draw_heat_map()
# fig_heat.savefig("heatmap.png")




# --- Fim da Fase 4: Implementação da análise de dados ---

# --- Início da Fase 5: Criação de visualizações e relatórios ---

# Gerar e salvar o gráfico categórico
# Chamamos a função draw_cat_plot que criamos
fig_cat = draw_cat_plot()
# Salvamos a figura gerada como um arquivo PNG
# O nome do arquivo será catplot.png
fig_cat.savefig("catplot.png")
print("Gráfico categórico salvo como catplot.png")

# Gerar e salvar o mapa de calor
# Chamamos a função draw_heat_map que criamos
fig_heat = draw_heat_map()
# Salvamos a figura gerada como um arquivo PNG
# O nome do arquivo será heatmap.png
fig_heat.savefig("heatmap.png")
print("Mapa de calor salvo como heatmap.png")

# --- Fim da Fase 5: Criação de visualizações e relatórios ---

