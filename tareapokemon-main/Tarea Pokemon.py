import pandas as pd
import matplotlib.pyplot as plt  #NOTA: SI NO LOS DEJA CORRER EL MATPLOTLIB Y SEABORN
import seaborn as sns            #APRETAR CTRL + P , escribir PYTHON y seleccionar interprete 3.11.X

#1. Lectura de datos
#- Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.
def cargar_datos():
    try: 
        file = "pokemon_primera_gen_datos_limpios.csv"
        pk = pd.read_csv(file)
        if pk.empty:
            print("Error: El archivo csv está vacío.")
            return None
 #Aquí más todo estoy como llenando del tipo 2 para evitar errores cuando esten los conteos xd
        pk["Tipo 2"] = pk["Tipo 2"].fillna("No posee")
        return pk
    except FileNotFoundError:
        print("Error: El archivo csv no fue encontrado. Revisa el nombre o la ruta.")
        return None
    except pd.errors.ParserError as e: #esto lo encontré en stackoverflow para poder evitar errores al leer el csv, es solo para asegurarnos, en el datawrangler vi cuestiones como repetidas xd
        print("Error de análisis en el archivo CSV: (e)")
        return None
#En la lectura de datos, carga el archivo de pokemon, pero hicimos otro archivo con los datos limpios en los que se aplicó el datawrangler 
# y de esa manera tenemos un archivo limpio y ese es el que lee el codigo en este trabajo 

#2. Filtrado y selección
#-----------------------
#- Filtra todos los Pokémon de tipo "Fuego".
#- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.

pk = cargar_datos() #funcion para cargar los datos limpios 

def filtrar_pokemon_fuego(pk):
    Fuego = pk[pk["Tipo 1"] == "Fuego"]
    filtrado = Fuego[["Nombre","Tipo 1","Tipo 2","Ataque","Velocidad"]] 
    #- puse el Tipo 2 como adicional por que algunos pokemons tienen segundo tipo
    return filtrado
pk_fuego = filtrar_pokemon_fuego(pk)

#3. Estadística descriptiva básica
#---------------------------------
#- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
def Estadisticas(pk):
    promedio = pk["Ataque"].mean()
    mediana = pk["Ataque"].median()
    moda = pk["Ataque"].mode()[0]

    print("\nPromedio: ",round(promedio),2) #redondea a que se muestren solo 2 decimales
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
    print("La desviacion estandar de de los Puntos de salud es de:",round(Desviacion,2))

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
    plt.title('Boxplot de Puntos de Salud por Tipo Principal (Tipo 1)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#- Grafica la distribución de la defensa usando un diagrama de violín.
def diagrama_violin(pk):
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=pk, x="Tipo 1", y="Defensa")
    plt.title('Diagrama de Violín de la Defensa por Tipo Principal')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#5. Manipulación de datos
#------------------------
#- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
#- Ordena el DataFrame por "Poder Total" de mayor a menor.

def nueva_columna(pk):
    df = pk.copy()
    df["Poder Total"] = df[["Ataque", "Defensa", "Velocidad", "PS"]].sum(axis=1)
    tabla_ordenada = df.sort_values(by="Poder Total", ascending=False)
    print("\n--- Top 15 Pokémon por Poder Total ---")
    print(tabla_ordenada[["Nombre", "Tipo 1", "Poder Total"]].head(15).to_string(index=False))
#CHIQUILLOS CAMBIÉ ESTO PORQUE CON ESTO CREO UNA COPIA PARA QUE SEA 
#MAS SEGURO PARA NO ALTERAR EL DATASET ORIGINAL EN SI, PORQUE FUNCIONABA BIEN CON 4 COLUMNAS, PERO MEJOR LA ASEGURÉ PORQUE QUE PASARIA SI NOS TOCARÁ SUMAR MAS COLUMNAS? XD
#NOS TOCARIA ESCRIBIR CALETA DE VECES ESO QUE ESTABA ANTES PS, ASI QUE YA CON ESTO TO TRANQUI :v 

#6. Agrupamiento y análisis por grupo
#-------------------------------------
#- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
#- ¿Qué tipo tiene el mayor promedio de velocidad?
#- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
def estadisticas_ataque_por_tipo(pk):
    promedio = pk.groupby("Tipo 1")["Ataque"].mean()
    mediana = pk.groupby("Tipo 1")["Ataque"].median()
    ds = pk.groupby("Tipo 1")["Ataque"].std()
    
    df_agrupado = pd.DataFrame({"Promedio": round(promedio, 2), "Mediana": mediana, "Desviación Est.": round(ds, 2)})
    print("\n--- Estadísticas de Ataque por Tipo 1 ---")
    print(df_agrupado.to_string())

def mayor_promedio_velocidad(pk):
    promedios = pk.groupby('Tipo 1')['Velocidad'].mean()
    tipo_mayor = promedios.idxmax()
    valor_mayor = promedios.max()
    print(f"\nEl tipo principal con mayor promedio de velocidad es: {tipo_mayor}")
    print(f"Con un promedio de: {round(valor_mayor, 2)}")

def pokemon_mayor_menor_ps_por_tipo(pk):
    idx_mayor = pk.groupby('Tipo 1')['PS'].idxmax()
    idx_menor = pk.groupby('Tipo 1')['PS'].idxmin()
    
    mayor_ps = pk.loc[idx_mayor, ['Tipo 1', 'Nombre', 'PS']]
    menor_ps = pk.loc[idx_menor, ['Tipo 1', 'Nombre', 'PS']]
    
    print("\n[ MAYOR PS POR TIPO ]")
    print(mayor_ps.to_string(index=False))
    print("\n[ MENOR PS POR TIPO ]")
    print(menor_ps.to_string(index=False))


#7. Análisis exploratorio (EDA)
#------------------------------
#- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
#- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
#- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
#- Identifica posibles outliers en los valores de ataque y PS usando boxplots.

def tipos_ataque_defensa(pk):
    ataque_promedio = pk.groupby('Tipo 1')['Ataque'].mean().round(1)
    defensa_promedio = pk.groupby('Tipo 1')['Defensa'].mean().round(1)
    
    print("\n--- Promedio de Ataque por Tipo 1 (Descendente) ---")
    print(ataque_promedio.sort_values(ascending=False).to_string())
    print("\n--- Promedio de Defensa por Tipo 1 (Descendente) ---")
    print(defensa_promedio.sort_values(ascending=False).to_string())

def correlacion_ataque_velocidad(pk):
    correlacion = pk['Ataque'].corr(pk['Velocidad'])
    print(f"\nEl coeficiente de correlación entre Ataque y Velocidad es: {round(correlacion, 3)}")
    if correlacion > 0:
        print("Interpretación: Existe una correlación positiva. A mayor ataque, suele haber mayor velocidad.")

def dispersion_ps_tipo(datos): # Sacamos el coeficiente de variacion para determinar que tan dispersos estan los PS por tipo 
    ps = datos.groupby('Tipo 1')['PS'].std() # desviacion estandar de los ps por tipo
    alpha = datos.groupby('Tipo 1')['PS'].mean() # media de los ps por tipo
    coeficiente_de_variacion = ps / alpha # coeficiente de variacion 
    print("tipo    desviacion_estandar    dispersion")    
    for tipo in coeficiente_de_variacion.index:
        desviacion_estandar = coeficiente_de_variacion[tipo]
        if desviacion_estandar < 0.1:
            coeficiente = "poco dispersos"
        elif desviacion_estandar < 0.3:
            coeficiente = "moderadamente dispersos"
        else:
            coeficiente = "altamente dispersos"
        print(f"{tipo:<12} {desviacion_estandar:<15.2f} {coeficiente:<25}")

#
#Use el :<12, :<15 y :<25 para ordenar los datos en columnas rectas (le pregunte a la ia, porfa profe no se enoje)
# fue por el bien visual
#

def boxplot_outliers(pk):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(y=pk['Ataque'], color='lightcoral')
    plt.title('Identificación de Outliers: Ataque')
    plt.ylabel('Valor de Ataque')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(y=pk['PS'], color='lightgreen')
    plt.title('Identificación de Outliers: PS')
    plt.ylabel('Puntos de Salud (PS)')
    
    plt.tight_layout()
    plt.show() # CHICOS DE MOMENTO LO DEJARÉ HASTA AHI, FALTARIA COMPLETAR EL MENU, LA INTERPRETACION DE RESULTADOS PS 

#8. Ejercicios de interpretación
#-------------------------------
#- Interpreta los resultados de los gráficos y estadísticas: ¿qué conclusiones puedes sacar sobre los Pokémon de la primera generación?
#- ¿Qué tipo de Pokémon sería "más balanceado" según las estadísticas? ¿Y el más especializado?
def interpretacion(pk):
    print("CONCLUSIONES GENERALES")
    conclusion = pk.groupby("Tipo 1")[["Ataque", "Defensa", "Velocidad", "PS"]].mean()
    conclusion["DIFERENCIA"] = conclusion.std(axis=1) #AXIS FUNCIONA PARA COMPARAR POR FILAS
    balanceado = conclusion["DIFERENCIA"].idxmin()
    especializado = conclusion["DIFERENCIA"].idxmax()
    #BALANCEADO
    print("TIPO MÁS BALANCEADO:", balanceado)
    print("PROMEDIO ATAQUE:", round(conclusion.loc[balanceado, "Ataque"], 2))
    print("PROMEDIO DEFENSA:", round(conclusion.loc[balanceado, "Defensa"], 2))
    print("PROMEDIO VELOCIDAD:", round(conclusion.loc[balanceado, "Velocidad"], 2))
    print("PROMEDIO PS:", round(conclusion.loc[balanceado, "PS"], 2))
    #ESPECIALIZADO
    print("TIPO MÁS ESPECIALIZADO:", especializado)
    print("PROMEDIO ATAQUE:", round(conclusion.loc[especializado, "Ataque"], 2))
    print("PROMEDIO DEFENSA:", round(conclusion.loc[especializado, "Defensa"], 2))
    print("PROMEDIO VELOCIDAD:", round(conclusion.loc[especializado, "Velocidad"], 2))
    print("PROMEDIO PS:", round(conclusion.loc[especializado, "PS"], 2))




##############Menus#################

def menuejercicio3():
    print("\nMenu para Estadísticas descriptivas básicas (Ejercicio 3).")
    print("1.- Estadisticas pokemons.")
    print("2.- Pokemon con mayor defensa y con menor velocidad.")
    print("3.- Pokemons con 2 tipos.")
    print("4.- Rango y la desviación estándar de los PS,")

    opcion2 = input("\nSeleccione una de las siguientes opciones (1-4):")

    if opcion2 == "1":
        Estadisticas(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion2 == "2":
        MayoryMenor(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion2 == "3":
        Dostipos(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion2 == "4":
        Saludpokemon(pk)
        input("\nPresiona Enter para continuar...")

    else:
        print("\nERROR ingrese una opcion valida:")



def menuejercicio4():
    print("\nMenu para Visualización de datos (ejercico 4).")
    print("1.- histograma de los valores de ataque.")
    print("2.- gráfico de dispersión entre ataque y velocidad.")
    print("3.- boxplot de los PS por tipo principal (Tipo 1).")
    print("4.- distribución de la defensa usando un diagrama de violín.")

    opcion3 = input("\nSeleccione una de las siguientes opcciones (1-4):")

    if opcion3 == "1":
        diagrama_histograma(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion3 == "2":
        diagrama_dispersion(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion3 == "3":
        diagrama_boxplot(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion3 == "4":
        diagrama_violin(pk)
        input("\nPresiona Enter para continuar...")

    else:
        print("\nERROR ingrese una opcion valida:")


def menuejercicio6():
    print("\nMenu Agrupamiento y análisis por grupo (Ejercicio 6).")
    print("1.- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).")
    print("2.- Tipo con el mayor promedio de velocidad.")
    print("3.- Pokémon con mayor y menor PS por tipo unico")

    opcion4 = input("\nSeleccione una de las siguientes opcciones (1-3):")

    if opcion4 == "1":
        estadisticas_ataque_por_tipo(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion4 == "2":
        mayor_promedio_velocidad(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion4 == "3":
        pokemon_mayor_menor_ps_por_tipo(pk)
        input("\nPresiona Enter para continuar...")
        
    else:
        print("\nERROR ingrese una opcion valida:")
        

def menuejercicio7():
    print("\nmenu Análisis exploratorio (EDA) (ejercicio 7)")
    print("1.- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa?")
    print("2.- Calcular el coeficiente de correlación entre ataque y velocidad.")
    print("3.- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)")
    print("4.- Identificar posibles outliers en los valores de ataque y PS usando boxplots.")

    opcion5 = input("\nSeleccione una de las siguientes opcciones (1-4):")

    if opcion5 == "1":
        tipos_ataque_defensa(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion5 == "2":
        correlacion_ataque_velocidad(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion5 == "3":
        dispersion_ps_tipo(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion5 == "4":
        boxplot_outliers(pk)
        input("\nPresiona Enter para continuar...")

    else:
        print("\nERROR ingrese una opcion valida:")


while True :
    print("\nMenu Principal.")
    ######## No hago una carga de datos, por que en teoria ya estan en un archivo txt externo o eso creo
    print("1.- Filtrado y selección (Ejercicio 2).")
    print("2.- Estadística descriptiva básica (Ejercicio 3).")
    print("3.- Visualización de datos (Ejercicio 4).")
    print("4.- Manipulación de datos (Ejercicio 5),")
    print("5.- Agrupamiento y análisis por grupo (Ejercicio 6).")
    print("6.- Análisis exploratorio (EDA) (Ejercicio 7).")
    print("7.- Ejercicios de interpretación (Ejercicio 8).")
    print("8.- Cerrar el programa.")

    opcion = input("\nSeleccione una opcion de las siguientes (1-8):")

    if opcion == "1":
        print("\n",pk_fuego)
        input("\nPresiona Enter para continuar...")

    elif opcion == "2":
        menuejercicio3()

    elif opcion == "3":
        menuejercicio4()

    elif opcion == "4":
        nueva_columna(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion == "5":
        menuejercicio6()

    elif opcion == "6":
        menuejercicio7()

    elif opcion == "7":
        interpretacion(pk)
        input("\nPresiona Enter para continuar...")

    elif opcion == "8":
        print("Cerrando el programa.")
        break

    else:
        print("\nERROR ingrese una opcion valida:")
        
