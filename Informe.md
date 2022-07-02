![logo](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/Aspose.Words.bd2c33f2-00cf-4bcb-b3d7-f43fc638a7f5.001.png)

**TRABAJO PARCIAL: GRAFOS** 

**CURSO: COMPLEJIDAD ALGORÍTMICA**

**PROFESOR: CANAVAL SÁNCHEZ, LUIS MARTIN**

**SECCIÓN: WV72**

**TRABAJO PRESENTADO POR:** 

** ⋅⋅* Vilca Morales, Fulgencio Marx		U201924289**

** ⋅⋅* Espinal Atencia, Jefferson William 		U201919607**

** ⋅⋅* Lopez Flores, Jose Rodrigo     		U201910421**

**CICLO ACADÉMICO: 2022-1**


**RESUMEN EJECUTIVO**

En el presente trabajo tiene como finalidad generar un grafo de forma eficiente con listas de adyacencia y guardarlos mediante un archivo de texto. Simulando una ciudad con más de 80 calles que generarán más de 1500 intersecciones. Además, se debe buscar las 3 rutas más cortas.


**IMAGEN ESTÁTICA DE LA CIUDAD O PORCIÓN DE CIUDAD ELEGIDA**

Para la realización del trabajo, nuestro grupo tomó en cuenta la ciudad de La Plata, que se encuentra ubicada en Argentina. Tomamos en cuenta un total de 86 calles, lo cual estaría representado por 42 filas y 44 columnas.


![Mapa](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/Aspose.Words.bd2c33f2-00cf-4bcb-b3d7-f43fc638a7f5.002.png)

![Diagrama](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/Aspose.Words.bd2c33f2-00cf-4bcb-b3d7-f43fc638a7f5.003.png)

![Mapa1](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/20930165-1d38-4991-8b24-2af0f192baff.png)


**DESCRIPCIÓN DE LOS DATOS CONSIGNADOS POR CALLE**

Para los datos de las calles de la ciudad elegida, serán un listado de los nombres de las calles, que estarán almacenadas en un archivo de texto.
Las calles que obtuvimos de la porción elegida de la ciudad fueron en total 86.


**DESCRIPCIÓN DE LA INFORMACIÓN CONSIGNADA POR INTERSECCIÓN**

En este caso, se decidió optar por la siguiente estructura:

Número de la intersección - Primera Calle - Segunda Calle - Latitud - Longitud

Donde:

●	Número de la intersección: El número que se asigna a cada intersección entre las diferentes calles, no puede repetirse.

●	Primera calle: Una de las calles que forma parte de la intersección 

●	Segunda calle: La segunda calle que forma parte de la intersección

●	Latitud y longitud: Coordenada de la intersección.

Además, estos datos estarían delimitados por un espacio en el .txt para su correspondiente lectura.

Datos de ejemplo:

0 Av.1 C.521 -34.885116 -57.976523

1 Av.1 C.522 -34.887932 -57.974166

2 Av.1 C.528 -34.891870 -57.967053

Las intersecciones que obtuvimos de la porción de la ciudad elegida fueron en total 1729.


**EXPLICACIÓN DE CÓMO SE ELABORÓ EL GRAFO, QUÉ REPRESENTAN LAS ARISTAS Y LOS VÉRTICES**

Para la elaboración del grafo, el primer paso es leer el archivo “Calles.txt” que contiene los nombres de las calles y almacenarlos en una lista. 

En la función “generarIntersecciones”, tendrá como parámetros la lista de calles, el archivo que contendrá la información de cada intersección, también el usuario debe especificar el número de calles que habrá tanto en vertical, como en horizontal y debe poner una lista vacía, ya que ahí se almacenará las coordenadas de cada intersección. Al ingresar los datos, se le asignará un número a cada calle por medio de un diccionario y se creará una matriz de -1 con el mismo número de filas y columnas. Luego, lee el archivo “Intersecciones con coordenadas.txt” para agregar el número que representa cada intersección dentro de la matriz que simulará la ciudad y estará lugar indicado gracias al diccionario. Si en caso no existe una intersección entre calles, el nodo quedará en -1.

Luego de simular la ciudad, empezaremos a generar el grafo con listas de adyacencia, esa función tendrá como parámetro la matriz que representa la ciudad, la coordenada y la hora de la ciudad. Definimos la dimensión de la matriz y después comprobamos si existen nodos adyacentes en cada intersección, calculamos la distancia entre los vértices con ayuda de la fórmula de Haversine y el factor tráfico con el algoritmo de Perlin. Finalmente, toda la lista de adyacencia la guardamos en un archivo de texto.

![Gráfico](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/Aspose.Words.bd2c33f2-00cf-4bcb-b3d7-f43fc638a7f5.004.png)


**EXPLICACIÓN DE CÓMO SE ELABORÓ EL FACTOR DE TRÁFICO**

Para la elaboración del factor de tráfico, el primer paso fue definir el algoritmo a utilizar, nuestro grupo optó por el algoritmo de ruido perlin, el cual produce una secuencia “suave” de números pseudoaleatorios que en nuestro caso nos permitirían simular de manera mucho más realista el flujo de tráfico en una ciudad.

Además, para generar un factor de ruido acorde a las diferentes horas puntas de tráfico, se implementó una función que dado una determinada hora, genera un ruido perlin con picos valores mucho más altos o más bajos, los cuales son asignados a cada vértice de modo que simula el tráfico en esa hora.

![Gráfico1](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/perlin.png)


**EXPLICACIÓN DE CÓMO SE GENERÓ LA DISTANCIA ENTRE INTERSECCIONES**

Para hallar la distancia entre intersecciones se utilizó el algoritmo Haversine, el cual dado la longitud y latitud de 2 puntos nos permite hallar su distancia.Su formula es la siguiente:

![Gráfico2](https://github.com/JeffersonEspinalA/TF-201910421-201919607-201924289/blob/main/Informe/Haversine.png)


**EXPLICACIÓN DE CÓMO SE BUSCA LOS 3 CAMINOS MÁS CORTOS**

Para conocer los caminos más cortos para llegar de una calle a otra se utilizó el algoritmo de Dijkstra con pequeños cambios. Estos cambios son 2 atributos, los cuales son el atributo ‘e’, que sirve al momento de que se haya llegado al nodo destino, y el otro es el atributo ‘p’, el cual es el peso mínimo que debe costar al destino. Cuando empieza a compilar el proyecto, p es igual 0, luego estará cambiando de valor al costo del nodo destino cada vez que se encuentre un nuevo camino. 

También está la función “path_visualization”, que es de mucha ayuda para mostrar solo el camino de inicio a fin. Las dos funciones anteriormente mencionadas estarán llamadas en la función “function_path”, para que sea más cómodo poner las argumentos. 


**CONCLUSIONES**

●	Fueron de mucha ayuda algunos temas aprendidos en clase como los grafos y el algoritmo de Dijkstra. Para simular el mapa de la ciudad de La Plata usamos la lista de adyacencia y por matriz. 

●	Usamos la matriz para poder saber los nodos adyacentes de cada nodo, y la lista de adyacencia para guardar las calles con sus respectivos pesos. Por otro lado, el algoritmo de Dijkstra para encontrar los caminos más cortos de un nodo a otro.
