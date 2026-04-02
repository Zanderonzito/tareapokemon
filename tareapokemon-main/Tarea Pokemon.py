import pandas as pd

# !!! FAVOR PODER FILLEAR MISSING VALUES EN DATA WRANGLER EN SUS PC´S, A MI NO ME DEJA HACERLO :(

#1. Lectura de datos
#- Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.
file = "pokemon_primera_gen_datos_limpios.csv"
df = pd.read_csv(file)
df.head()
#2. Filtrado y selección
#-----------------------
#- Filtra todos los Pokémon de tipo "Fuego".
#- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
fuego = df[df["Tipo 1"] == "Fuego"]
print("=== Pokémon de tipo Fuego ===")
print(fuego)

columnas = df[["Nombre", "Tipo 1", "Ataque", "Velocidad"]]
print("\n=== Columnas seleccionadas ===")
print(columnas.head())



