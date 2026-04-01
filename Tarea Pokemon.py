import pandas as pd
#1. Lectura de datos
#-------------------
#- Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.
def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna({'Nombre': "No posee"})
    df = df.fillna({'Tipo 2': "No posee"})
    return df
df = pd.read_csv(r'c:\Users\X-40845\Desktop\pokemon_primera_gen.csv')

df_clean = clean_data(df.copy())
df_clean.head()

#2. Filtrado y selección
#-----------------------
#- Filtra todos los Pokémon de tipo "Fuego".
#- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.


