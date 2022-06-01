![logo](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/Aspose.Words.bd2c33f2-00cf-4bcb-b3d7-f43fc638a7f5.001.png)
<center>**UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS**</center>

**TRABAJO PARCIAL: GRAFOS** 

**CURSO: COMPLEJIDAD ALGORÍTMICA**

**PROFESOR: CANAVAL SÁNCHEZ, LUIS MARTIN**

**SECCIÓN: WV72**

**TRABAJO PRESENTADO POR:** 

**Vilca Morales, Fulgencio Marx		U201924289**

**Espinal Atencia, Jefferson William 		U201919607**

**Lopez Flores, Jose Rodrigo     		U201910421**








**CICLO ACADÉMICO: 2022-1**
# Índice
**Resumen ejecutivo3**

**Imagen estática de la ciudad o porción de ciudad elegida3**

**Descripción de los datos consignados por calle4**

**Descripción de la información consignada por intersección4**

**Explicación de cómo se elaboró el grafo4**

**Enlaces5**













**RESUMEN EJECUTIVO**

En el presente trabajo tiene como finalidad generar un grafo de forma eficiente con listas de adyacencia y guardarlos mediante un archivo de texto. Simulando una ciudad con más de 80 calles que generarán más de 1500 intersecciones.


**IMAGEN ESTÁTICA DE LA CIUDAD O PORCIÓN DE CIUDAD ELEGIDA**

Para la realización del trabajo, nuestro grupo tomó en cuenta la ciudad de La Plata, que se encuentra ubicada en Argentina. Tomamos en cuenta un total de 86 calles, lo cual estaría representado por 42 filas y 44 columnas.


![Mapa](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/Aspose.Words.bd2c33f2-00cf-4bcb-b3d7-f43fc638a7f5.002.png)


![Diagrama](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/Aspose.Words.bd2c33f2-00cf-4bcb-b3d7-f43fc638a7f5.003.png)





**DESCRIPCIÓN DE LOS DATOS CONSIGNADOS POR CALLE**

Para los datos de las calles de la ciudad elegida, serán un listado de los nombres de las calles y estas estarán almacenadas en un archivo de texto.


**DESCRIPCIÓN DE LA INFORMACIÓN CONSIGNADA POR INTERSECCIÓN**

En este caso, se decidió optar por la siguiente estructura:

<Número de la intersección>-<Primera Calle>-<Segunda Calle>

Donde;

●	Número de la intersección: El número que se asigna a cada intersección entre las diferentes calles, no puede repetirse.

●	Primera calle: Una de las calles que forma parte de la intersección 

●	Segunda calle: La segunda calle que forma parte de la intersección

Además, estos datos estarían delimitados por un espacio en el .txt para su correspondiente lectura.

Datos de ejemplo:

0 Av.1 C.521

1 Av.1 C.522

2 Av.1 C.528

3 Av.1 C.529

4 Av.1 C.530


**EXPLICACIÓN DE CÓMO SE ELABORÓ EL GRAFO, QUÉ REPRESENTAN LAS ARISTAS Y LOS VÉRTICES.**

Para la elaboración del grafo, el primer paso es leer el archivo “Calles.txt” que contiene los nombres de las calles y almacenarlos en una lista. 

En la función “generarIntersecciones”, tendrá como parámetros la lista de calles, el archivo que contendrá la información de cada intersección, y el usuario debe especificar el número de calles que habrá tanto en vertical, como en horizontal. Al ingresar los datos, se le asignará un número a cada calle por medio de un diccionario y se creará una matriz de -1 con el mismo número de filas y columnas. Luego, lee el archivo “Intersecciones.txt” para agregar el número que representa cada intersección dentro de la matriz que simulará la ciudad y estará lugar indicado gracias al diccionario. Si en caso no existe una intersección entre calles, el nodo quedará en -1.

Luego de simular la ciudad, empezaremos a generar el grafo con listas de adyacencia, esa función tendrá como parámetro la matriz que representa la ciudad. Definimos la dimensión de la matriz y después comprobamos si existen nodos adyacentes en cada intersección. Finalmente, toda la lista de adyacencia la guardamos en un archivo de texto.

Las calles representan las aristas, mientras que las intersecciones entre calles representan los vértices. Cada intersección estará identificada por un número.

![Gráfico](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/Aspose.Words.bd2c33f2-00cf-4bcb-b3d7-f43fc638a7f5.004.png)

**Enlaces**

Enlace del código: <https://colab.research.google.com/drive/1rtDkZim6BxKHasFDG-tx02czOUBXoaUS?usp=sharing>

Enlace del video de la exposición: <https://youtu.be/28MDeOXMyyI>

