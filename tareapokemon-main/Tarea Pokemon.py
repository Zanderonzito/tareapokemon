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
def Estadisticas(pk):
    promedio = pk["Ataque"].mean()
    mediana = pk["Ataque"].median()
    moda = pk["Ataque"].mode()[0]

    print("Promedio: ",round(promedio))
    print("Mediana: ",mediana)
    print("Moda: ",moda)

#- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
def MayoryMenor(pk):
    Mayordefensa = pk.loc[pk["Defensa"].idxmax()]
    Menorvelocidad = pk.loc[pk["Velocidad"].idxmin()]
    print("El pokemon com mas defensa es: ",Mayordefensa["Nombre"],"con un total de:",Mayordefensa["Defensa"])
    print("El pokemon con menor velocidad es:",Menorvelocidad["Nombre"],"con un total de:",Menorvelocidad["Velocidad"])

#- ¿Cuántos Pokémon tienen dos tipos?
def Dostipos(pk):
    Numero = pk[pk["Tipo 2"] != "No posee"].shape[0]
    print("Hay",Numero,"pokemons con 2 tipos")

#- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).
def Saludpokemon(pk):
    Rango = pk["PS"].max() - pk["PS"].min()
    Desviacion = pk["PS"].std()
    print("El rango Puntos de salud de los pokemons es de:",Rango)
    print("La desviacion estandar de de los Puntos de salud es de:",round(Desviacion))

#muestra los datos para luego agregar a un menu
print (Estadisticas(pk))
print (MayoryMenor(pk))
print(Dostipos(pk))
print(Saludpokemon(pk))
#El que haga el menu, que tambien haga un segundo menu para este ejercicio (3)
