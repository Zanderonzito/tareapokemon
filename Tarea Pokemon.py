import pandas as pd
#1. Lectura de datos
#- Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.
def clean_data(pokemones):
    pokemones = pokemones.drop_duplicates()
    pokemones = pokemones.fillna({'Nombre': "No posee"})
    pokemones = pokemones.fillna({'Tipo 2': "No posee"})
    return pokemones
pokemones = pd.read_csv(r'c:\Users\X-40845\Desktop\pokemon_primera_gen.csv')

pokemones_clean = clean_data(pokemones.copy())
pokemones_clean.head()

#2. Filtrado y selección
#-----------------------
#- Filtra todos los Pokémon de tipo "Fuego".
#- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.


