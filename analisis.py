# %%
# Importamos librerias necesarias
# Manipulación & convertir a arrays
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Visualización:
import seaborn as sns
import plotly.graph_objects as go

# %%
# Definimos Funciones


def shifted_value(df, newcol, col, days):
    """function to shift values xDays"""
    df2 = df.copy()
    df2[newcol] = np.array(file.set_index(['TIM_DAY']).sort_index(ascending=False)[
        col].shift(days).copy())

    return df2
# %%


# Leemos el archivo
file = pd.read_csv('searchAll.csv')
file = file[file['VERTICAL_CATEG_NAME'] == 'ROPA Y ACCESORIOS']
# %%

cols_to_use = ['TIM_DAY', 'COST_SEARCH', 'IMPRESIONES_SEARCH',
               'CLICS_SEARCH', 'CONVERSION_VALUE_SEARCH']
file = file[cols_to_use]

# analisis['TIM_DAY'] = pd.to_datetime(analisis['TIM_DAY'])

# analisis

columns_to_shift = ['COST_SEARCH', 'IMPRESIONES_SEARCH',
                    'CLICS_SEARCH', 'CONVERSION_VALUE_SEARCH']
for column in columns_to_shift:
    columnName = column + '_Ayer'
    file = shifted_value(file, columnName, column, -1)
# Calculamos valores semana pasada
for column in columns_to_shift:
    columnName = column + '_LastWeek'
    file = shifted_value(file, columnName, column, -7)
file = file.dropna()
# %%
# sns.pairplot(file)
# %%

file['TIM_DAY'] = pd.to_datetime(file['TIM_DAY'])
file = file.sort_values('TIM_DAY')
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=file['TIM_DAY'],
                         y=file['CONVERSION_VALUE_SEARCH'].pct_change()))
fig.add_trace(go.Scatter(x=file['TIM_DAY'],
                         y=file['COST_SEARCH'].pct_change()))
fig.show()
# %%
