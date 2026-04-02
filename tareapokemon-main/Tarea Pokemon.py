import pandas as pd

# !!! FAVOR PODER FILLEAR MISSING VALUES EN DATA WRANGLER EN SUS PC´S, A MI NO ME DEJA HACERLO :(

#1. Lectura de datos
#- Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.
file = "pokemon_primera_gen_datos_limpios.csv"
pk = pd.read_csv(file)
pk.head()


#2. Filtrado y selección
#-----------------------
#- Filtra todos los Pokémon de tipo "Fuego".
#- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
#- puse el Tipo 2 como adicional por que algunos pokemons tienen segundo tipo

def filtrar_pokemon_fuego(pk):
    Fuego = pk[pk["Tipo 1"] == "Fuego"]
    filtrado = Fuego[["Nombre","Tipo 1","Tipo 2","Ataque","Velocidad"]]
    return filtrado

#Mostrar datos para luego agregar a un menu
pk_fuego = filtrar_pokemon_fuego(pk)
print(pk_fuego)


#3. Estadística descriptiva básica
#---------------------------------
#- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
#- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
#- ¿Cuántos Pokémon tienen dos tipos?
#- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).

#no tengo idea de como hacer un comit

