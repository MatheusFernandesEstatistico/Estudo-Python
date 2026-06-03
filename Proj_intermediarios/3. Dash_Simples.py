from shiny import App, render, ui, reactive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gerando dados de exemplo para o dashboard
dados_vendas = pd.DataFrame({
    'data': pd.date_range('2024-01-01', periods=100, freq='D'),
    'produto': np.random.choice(['A', 'B', 'C', 'D'], 100),
    'vendas': np.random.normal(1000, 200, 100).round(2),
    'custo': np.random.normal(700, 150, 100).round(2),
    'satisfacao': np.random.uniform(3, 5, 100).round(1),
    'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 100)
})

dados_vendas['lucro'] = dados_vendas['vendas'] - dados_vendas['custo']

