[[modelo_logit]]
La clasificación surge como respuesta a los problemas en los que la variable que queremos predecir es discreta o categórica.

En la regresión lineal podemos incorporar variables explicativas categóricas mediante técnicas como la codificación _one-hot_ o la creación de variables _dummy_. Sin embargo, la situación cambia cuando la propia variable que queremos predecir es categórica. En ese caso, ya no buscamos estimar una variable continua, sino determinar a qué categoría pertenece cada observación.

## Variables continuas y discretas

Una variable continua cambia de manera gradual: un pequeño incremento en su valor representa un pequeño cambio en la magnitud observada. Las variables discretas, en cambio, presentan saltos entre categorías.

Además, no siempre es posible establecer que una categoría sea mayor o mejor que otra. Algunas variables categóricas sí admiten un orden. Por ejemplo, el máximo nivel educativo alcanzado podría organizarse de la siguiente manera:

1. Educación primaria.
    
2. Educación secundaria.
    
3. Educación universitaria.
    

En este caso existe un orden, pero las distancias entre las categorías no necesariamente son equivalentes. El paso de la educación primaria a la secundaria no tiene por qué representar el mismo cambio que el paso de la secundaria a la universidad.

Existen también variables categóricas para las que ni siquiera puede establecerse un orden. Estas características hacen que la regresión lineal no resulte adecuada, en general, para resolver problemas de clasificación.

## El objetivo de la clasificación

El punto de partida es similar al de una regresión lineal: contamos con una o varias variables explicativas y queremos estudiar cómo influyen sobre una variable de respuesta.

Supongamos, por ejemplo, que un banco desea predecir si un cliente pagará o no una deuda. La variable de respuesta tiene dos categorías:

- Paga.
    
- No paga.
    

Se trata, por lo tanto, de un problema de clasificación binaria. En particular, podríamos estar interesados en calcular la probabilidad de que el cliente no pague.

Una posible variable explicativa sería el ingreso de la persona, ya que probablemente influya en su capacidad de pago. Podríamos analizar, mediante un diagrama de cajas, cómo se distribuyen los ingresos entre quienes pagan y quienes no lo hacen.

Es posible que el ingreso, por sí solo, no permita distinguir claramente ambos grupos. Otra variable, como el saldo deudor o _balance_ del cliente, podría ofrecer una separación más clara: cuanto mayor sea su deuda acumulada, mayor podría ser la probabilidad de incumplimiento.

## Estimación de probabilidades

Los métodos de clasificación suelen abordar el problema mediante la estimación de una probabilidad. Aunque la variable final sea categórica, el modelo calcula primero un valor continuo comprendido entre 0 y 1.

En el ejemplo anterior, el modelo podría estimar la probabilidad de que un cliente no pague. Luego, esa probabilidad se transforma en una clasificación mediante un umbral. Por ejemplo:

- Si la probabilidad estimada es igual o superior a 0,5, se clasifica al cliente como “no paga”.
    
- Si es inferior a 0,5, se lo clasifica como “paga”.
    

El umbral de 0,5 es una posibilidad habitual, aunque puede modificarse según las características y los objetivos del problema.

## Limitaciones de la regresión lineal

En un problema binario podríamos codificar la variable de respuesta de la siguiente manera:

- `1`: el cliente no paga.
    
- `0`: el cliente paga.
    

Después, podríamos aplicar una regresión lineal y utilizar 0,5 como umbral de clasificación. No obstante, este enfoque presenta un inconveniente importante: la regresión lineal puede producir valores inferiores a 0 o superiores a 1, los cuales no pueden interpretarse correctamente como probabilidades.

Cuando existen más de dos categorías, las dificultades son aún mayores. Para utilizar una regresión lineal necesitaríamos asignarles valores numéricos y suponer que:

1. Las categorías tienen un orden definido.
    
2. La distancia entre categorías consecutivas es equivalente.
    

Estas condiciones rara vez se cumplen. Además, cambiar arbitrariamente el orden o la codificación de las categorías podría alterar por completo las predicciones.

## Regresión logística

Debido a estas limitaciones, necesitamos métodos diseñados específicamente para problemas de clasificación. Uno de los primeros que estudiaremos es la **regresión logística**.

Este modelo permite estimar probabilidades manteniendo los resultados dentro del intervalo de 0 a 1. A partir de esas probabilidades, podemos asignar cada observación a una de las categorías posibles.

La regresión logística será, por lo tanto, nuestro punto de partida para estudiar los métodos de clasificación.