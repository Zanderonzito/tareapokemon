import pandas as pd
import matplotlib.pyplot as plt  #NOTA: SI NO LOS DEJA CORRER EL MATPLOTLIB Y SEABORN
import seaborn as sns            #APRETAR CTRL + P , escribir PYTHON y seleccionar interprete 3.11.X

#AL TERMINAR LOS EJERCICIOS MEJOR HAGAMOS UN MENU GLOBAL?

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

#5.Manipulación de Datos
#------------------------
#- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
#- Ordena el DataFrame por "Poder Total" de mayor a menor.
def nueva_columna (datos):
    datos["poder_total"] = datos["Ataque"] + datos["Defensa"] + datos["Velocidad"] + datos["PS"]
    Data_frame_ordenada = datos.sort_values(by = "poder_total", ascending = False)

def Agrupamiento(datos):
    promedio = datos.groupby(by = "Tipo 1")["Ataque"].mean()
    mediana = datos.groupby(by = "Tipo 1")["Ataque"].median()
    ds = datos.groupby(by = "Tipo 1")["Ataque"].std()
    print("\nPromedio:")    
    print(round(promedio, 2))
    print("\nMediana:")
    print(mediana)
    print("\nDesviacion estandar:")
    print(round(ds, 2))


#muestra los datos para luego agregar a un menu
print (Estadisticas(pk))
print (MayoryMenor(pk))
print(Dostipos(pk))
print(Saludpokemon(pk))
print(nueva_columna(pk))
Agrupamiento(pk)
#El que haga el menu, que tambien haga un segundo menu para este ejercicio (3)

#4. Visualización de datos
#---------------------------------
#- Haz un histograma de los valores de ataque.
def diagrama_histograma(pk):
    plt.figure(figsize=(8, 5))
    plt.hist(pk["Ataque"], bins=20, color="steelblue", edgecolor="black")
    plt.title("Distribución del Ataque")
    plt.xlabel("Ataque")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

#- Realiza un gráfico de dispersión entre ataque y velocidad.
def diagrama_dispersion(pk):
    plt.figure(figsize=(8, 5))
    plt.scatter(pk["Ataque"], pk["Velocidad"], color="coral", edgecolors="black", alpha=0.7)
    plt.title("Ataque vs Velocidad")
    plt.xlabel("Ataque")
    plt.ylabel("Velocidad")
    plt.tight_layout()
    plt.show()

#- Haz un boxplot de los PS por tipo principal (Tipo 1).
def diagrama_boxplot(pk):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=pk, x="Tipo 1", y="PS")
    plt.title("PS por Tipo Principal")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#- Grafica la distribución de la defensa usando un diagrama de violín.
def diagrama_violin(pk):
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=pk, x="Tipo 1", y="Defensa")
    plt.title("Distribución de Defensa por Tipo")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#7. Análisis exploratorio (EDA)
#------------------------------
#- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
def tipos_ataque_defensa(pk):
    print("PROMEDIO DE ATAQUE Y DEFENSA SEPARADO EN TIPOS")
    resumen = pk.groupby("Tipo 1")[["Ataque", "Defensa"]].mean()       #SEPARACIÓN DE TIPOS Y CALCULO DE PROMEDIO DE ATAQUE Y DEFENSA Y COMPARACIÓN DE ESTADISTICAS MÁS ALTAS QUE EL PROMEDIO
    resumen = resumen.sort_values(by="Ataque", ascending=False)        #ORDENAMIENTO TIPO SORT DE MAYOR A MENOR
    print(round(resumen, 2).to_string())                               #REDONDEO DE 2 DECIMALES,PARA EL CASO DE NUMEROS PERIODICOS
