# Rompecabeza lineal:
Dada una permutación cualquiera de la secuencia [4, 1, 3, 2]:
- Determinar cómo construiríamos otra secuencia que satisfaga la siguiente secuencia [1,2,3,4]
- Para construir una nueva secuencia solo podemos intercambiar dos números que estén en posiciones consecutivas de la secuencia. Por ejemplo, partiendo de la secuencia de partida [1, 2, 3, 4], solo sería posible generar las siguientes secuencias:
    - [**2**, **1**, 3, 4]
    - [1, **3**, **2**, 4]
    - [1, 2, **4**, **3**]

## 1. Primera parte
Se ha de definir el espacio de estado:

### 1.1. Modelización del entorno (estados)
La forma que tenemos para poder modelar el entorno es mediante la realización de observaciones que nos permiten definir todos los estados posibles del propio entorno. Por ello todos los estados posibles de un rompecabeza lineal [1,2,3,4] sería todas las combinaciones posibles. Esto resulta sencillo y sería esa característica observable y directa. Esto sería: 4*3*2*1 ó 4! Por ejemplo: [4,3,2,1], [3,1,2,4]...

### 1.2. Modelización de las acciones
Se trata de encontrar todas las transiciones posibles y encontrar el factor de ramificación. En este caso, se debe hacer caso a las restricciones que se determinan en las posibilidades de transicionar una secuencia X, de forma que se intercambien solo dos números que estén en posiciones consecutivas por cada unidad de tiempo discreto. Estas serían las acciones posibles:
- rotar los primeros 2 números de la izquierda de la cadena.
- rotar los 2 números centrales de la cadena.
- rotar los 2 números de la derecha de la cadena.

En cualquier momento dado, estas son las únicas acciones que producen transiciones de estados posibles y determinan el factor de ramificación, que sería de **3**.

Estas acciones las podemos llevar a cabo mediante 3 operadores distintos o con 1 solo operador y un parámetro de entrada que indique la posición (izquierda, centro o derecha) en la que aplicar el intercambio.

Aquí opto por la realización de un solo operador que recibe un parámetro de posición.

## 1. Definición del problema
El problema inicial  será el de llegar a una cadena específica [1,2,3,4] partiendo de una cadena inicial.

He optado por la definición de una solución única para este problema concreto aunque perfectamente podría haber no una única solución y entonces sería necesario valorar otros aspectos para determinar la optimización.

**La función objetivo _def f(x) -> bool:_** simplemente, para este problema en particular, verifica que dada cualquier representación de estado (una cadena [x,y,z,w]), el mismo es o no igual al estado (a la cadena de estado) [1,2,3,4]. Se trataría de una simple función booleana de verificación.

