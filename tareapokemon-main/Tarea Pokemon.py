import pandas as pd
import matplotlib.pyplot as plt  #NOTA: SI NO LOS DEJA CORRER EL MATPLOTLIB Y SEABORN
import seaborn as sns            #APRETAR CTRL + P , escribir PYTHON y seleccionar interprete 3.11.X

#AL TERMINAR LOS EJERCICIOS MEJOR HAGAMOS UN MENU GLOBAL? SI HAGAMOS UN MENU GLOBAL PARA QUE NO SE CORRA TODO AL TIRO

#1. Lectura de datos
#- Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.
def cargar_datos():
    try: 
        file = "pokemon_primera_gen.csv"
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
        print(f"Error de análisis en el archivo CSV: {e}")
        return None
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

    print("Promedio: ",round(promedio),2)
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
<<<<<<< HEAD
    print(f"\nEl rango de Puntos de Salud (PS) es de: {Rango}")
    print(f"La desviación estándar de los PS es de: {round(Desviacion, 2)}") #aqui solamente puse lo del 2 para lo del redondeo y que no pase de los dos decimales, tipo pa que no se muestren muchos decimales y ya
=======
    print("El rango Puntos de salud de los pokemons es de:",Rango)
    print("La desviacion estandar de de los Puntos de salud es de:",round(Desviacion),2)
>>>>>>> 2b78d1a17ef74a4b0e88bcf54c237a9c99eeae83

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

#5.Manipulación de Datos
df = pk.copy()
def nueva_columna():
    df["Poder Total"] = df[["Ataque", "Defensa", "Velocidad", "PS"]].sum(axis=1)
    tabla_ordenada = df.sort_values(by="Poder Total", ascending=False)
    print("\n--- Top 15 Pokémon por Poder Total ---")
    print(tabla_ordenada[["Nombre", "Tipo 1", "Poder Total"]].head(15).to_string(index=False)) #CHIQUILLOS CAMBIÉ ESTO PORQUE CON ESTO CREO UNA COPIA PARA QUE SEA 
#MAS SEGURO PARA NO ALTERAR EL DATASET ORIGINAL EN SI, PORQUE FUNCIONABA BIEN CON 4 COLUMNAS, PERO MEJOR LA ASEGURÉ PORQUE QUE PASARIA SI NOS TOCARÁ SUMAR MAS COLUMNAS? XD
#NOS TOCARIA ESCRIBIR CALETA DE VECES ESO QUE ESTABA ANTES PS, ASI QUE YA CON ESTO TO TRANQUI :v 
#///////////////////////////// 6 AGRUPAMIENTO Y ANALISIS POR GRUPO  /////////////////////////////////////
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


#muestra los datos para luego agregar a un menu
print (Estadisticas(pk))
print (MayoryMenor(pk))
print(Dostipos(pk))
print(Saludpokemon(pk))
print(nueva_columna(pk))
Agrupamiento(pk)
#El que haga el menu, que tambien haga un segundo menu para este ejercicio (3)
#7. Análisis exploratorio (EDA)
#------------------------------
#- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
#def tipos_ataque_defensa(pk):
 #   print("PROMEDIO DE ATAQUE Y DEFENSA SEPARADO EN TIPOS")            
  #  resumen = pk.groupby("Tipo 1")[["Ataque", "Defensa"]].mean()       #SEPARACIÓN DE TIPOS [1] , y TOMA DE PROMEDIO DE ATAQUE Y DEFENSA //AHORA SI QUE HACE POCO ME ENREDE JSJS
   #resumen = resumen.sort_values(by="Ataque", ascending=False)        #ORDENAMIENTO DE TABLA DE MAYOR A MENOR
    #print(round(resumen, 2).to_string())                               #REDONDEO DE 2 DECIMALES,PARA EL CASO DE NUMEROS PERIODICOS
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

def dispersion_ps_por_tipo(pk):
    desviacion = pk.groupby('Tipo 1')['PS'].std()
    print("\n--- Dispersión (Desviación Estándar) de PS por Tipo 1 ---")
    print(round(desviacion.sort_values(ascending=False), 2).to_string())

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
