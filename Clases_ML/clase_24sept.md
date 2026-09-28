# Clasificación I — Anaconda y Regresión Logística

**Curso:** Analítica de Datos II  
**Modalidad:** Teórico-práctica  
**Herramientas:** Python · scikit-learn · pandas · Anaconda Notebooks · GitHub  
**Tema central:** Introducción a problemas de clasificación y regresión logística

---

# 0. Objetivos de la clase

Al finalizar la clase, los estudiantes deberían poder:

- Diferenciar un problema de **regresión** de uno de **clasificación**.
- Entender qué estima una **regresión logística**.
- Comprender la función sigmoide y el papel del predictor lineal.
- Interpretar conceptualmente los coeficientes mediante **log-odds** y **odds**.
- Entender el papel del **umbral de clasificación**.
- Diferenciar falsos positivos y falsos negativos.
- Implementar una regresión logística básica con `scikit-learn`.
- Preparar datos numéricos y categóricos.
- Introducir la lógica de `OneHotEncoder`, `StandardScaler` y `Pipeline`.
- Entender por qué una accuracy elevada **no implica necesariamente un buen clasificador**.

---

# MÓDULO 1 — Entorno de trabajo: Anaconda, Colab y GitHub

## 1.1. Idea que quiero transmitir

Python no es Google Colab.

Colab es solamente uno de los posibles entornos para trabajar con Python. Conviene que los estudiantes conozcan otras formas de organizar un proyecto de análisis de datos.

En esta clase mostrar **Anaconda Notebooks** como alternativa.

## 1.2. ¿Por qué mostrar Anaconda?

Ventajas a enfatizar:

- Permite una organización más parecida a un proyecto local.
- Los archivos permanecen dentro del espacio de trabajo.
- Se pueden guardar:
  - notebooks `.ipynb`;
  - scripts `.py`;
  - bases de datos;
  - archivos auxiliares.
- Facilita separar distintas partes del proyecto.
- Permite trabajar con **entornos y kernels**.
- Se acerca más al flujo de trabajo que después van a encontrar trabajando localmente.

### Comparación conceptual

**Google Colab**

- Muy sencillo para compartir un notebook.
- Excelente para comenzar rápidamente.
- Muy integrado con Google Drive.
- El entorno de ejecución es temporal.
- Hay que gestionar archivos externos/Drive.

**Anaconda**

- Mayor lógica de proyecto.
- Persistencia de archivos.
- Scripts + notebooks + datos en una misma estructura.
- Mejor aproximación al trabajo local.
- Introduce naturalmente entornos, kernels y dependencias.

> No plantear Anaconda como “mejor que Colab”, sino como **otra herramienta con una lógica de trabajo diferente**.

---

# MÓDULO 2 — GitHub y reproducibilidad

## 2.1. GitHub

Explicar brevemente:

- repositorio de código;
- control de versiones;
- código abierto;
- posibilidad de compartir proyectos;
- enorme cantidad de implementaciones disponibles;
- vínculo cada vez más importante entre programación, ciencia de datos e IA.

Los notebooks de la clase están disponibles en GitHub con enlaces para abrirlos en:

- Google Colab;
- Anaconda Notebook.

## 2.2. Scripts `.py` y modularización

Mostrar que no todo debe quedar dentro de un único notebook.

Ejemplo:

```text
proyecto/
│
├── datos/
├── procesamiento.py
├── modelo.ipynb
└── resultados/
```

Idea pedagógica:

> Cuando un proyecto crece, conviene separar procesamiento, funciones y modelado.

Esto evita copiar y pegar continuamente el mismo código.

---

# MÓDULO 3 — Entornos, kernels y versiones

Introducción breve, sin profundizar demasiado.

## ¿Por qué existen los entornos?

Las librerías cambian.

Una actualización de:

- pandas;
- NumPy;
- scikit-learn;

puede modificar comportamientos o romper código antiguo.

Los entornos permiten especificar las versiones utilizadas en un proyecto.

Ejemplo conceptual:

```bash
conda create -n analitica python=3.12
conda activate analitica
```

### Idea clave

> Reproducibilidad no significa solamente compartir el código. También implica poder reconstruir el entorno en el que ese código funcionaba.

### Nota para próxima edición

**No extender demasiado esta sección.**

Objetivo aproximado: **15–20 minutos como máximo entre Anaconda + GitHub + entornos.**

Binder puede mencionarse como alternativa, pero no hace falta demostrarlo salvo que esté previamente probado.

---

# MÓDULO 4 — Introducción a clasificación

Pasar ahora al tema central.

Hasta ahora trabajamos principalmente con problemas donde:

\[
Y \in \mathbb{R}
\]

Por ejemplo:

- salario;
- precio;
- ventas;
- temperatura.

Ahora queremos predecir **categorías**.

Ejemplos:

- aprueba / no aprueba;
- paga / no paga;
- fraude / no fraude;
- gato / perro.

En clasificación binaria:

\[
Y \in \{0,1\}
\]

---

# MÓDULO 5 — Ejemplo introductorio: horas de estudio

Utilizar una base simulada.

Variables:

- \(X\): horas de estudio.
- \(Y\): resultado del examen.

Definir:

\[
Y=
\begin{cases}
1 & \text{aprueba}\\
0 & \text{no aprueba}
\end{cases}
\]

Mostrar el scatter:

- eje X: horas estudiadas;
- eje Y: 0/1.

### Pregunta a los estudiantes

> Si ya conocemos regresión lineal, ¿por qué no ponemos simplemente una recta?

---

# MÓDULO 6 — ¿Por qué no utilizar regresión lineal?

Problemas principales:

### 1. Las predicciones no están acotadas

Una regresión lineal puede producir:

\[
\hat{Y}<0
\]

o

\[
\hat{Y}>1
\]

y esos valores no pueden interpretarse directamente como probabilidades.

### 2. La relación entre X y probabilidad no tiene por qué ser lineal

Normalmente esperamos algo semejante a:

- cambios pequeños en los extremos;
- cambios mayores alrededor de la zona de incertidumbre.

Esto conduce a una función en forma de **S**.

---

# MÓDULO 7 — Regresión logística

Partimos de un predictor lineal:

\[
z=\beta_0+\beta_1X
\]

pero transformamos \(z\) mediante la función logística:

\[
P(Y=1|X)=\frac{1}{1+e^{-z}}
\]

La función sigmoide transforma:

\[
(-\infty,+\infty)
\]

en:

\[
(0,1)
\]

Por eso puede interpretarse como una probabilidad.

---

# MÓDULO 8 — Experimento con los coeficientes

Utilizar gráficos para modificar manualmente:

- \(\beta_0\);
- \(\beta_1\).

## Cambiar \(\beta_0\)

Desplaza horizontalmente la curva.

## Cambiar \(\beta_1\)

Modifica:

- dirección;
- pendiente;
- velocidad de transición entre probabilidades bajas y altas.

### Casos

\[
\beta_1>0
\]

La probabilidad aumenta con X.

\[
\beta_1<0
\]

La probabilidad disminuye con X.

\[
\beta_1=0
\]

X no modifica la probabilidad.

### Preguntas

> Si \(\beta_1>0\), ¿qué ocurre cuando aumenta X?

Después:

> ¿La probabilidad aumenta siempre exactamente la misma cantidad?

La segunda pregunta conduce al punto central:

**la regresión logística no es lineal en probabilidades.**

---

# MÓDULO 9 — Interpretación: odds y log-odds

Definir los odds:

\[
Odds=\frac{p}{1-p}
\]

Ejemplo:

Si:

\[
p=0.75
\]

entonces:

\[
Odds=\frac{0.75}{0.25}=3
\]

Interpretación:

> El evento es tres veces más probable que su no ocurrencia.

La regresión logística modela:

\[
\log\left(\frac{p}{1-p}\right)
=
\beta_0+\beta_1X
\]

Por lo tanto:

- \(\beta_1\) representa un cambio en **log-odds**;
- \(e^{\beta_1}\) representa el multiplicador de los **odds**.

### IMPORTANTE

Si:

\[
\beta_1=2
\]

una unidad adicional de X:

- suma 2 a los log-odds;
- multiplica los odds por:

\[
e^2\approx7.39
\]

No significa que la probabilidad aumente dos unidades ni que los odds se multipliquen por 2.

---

# MÓDULO 10 — Efectos sobre probabilidades

Mostrar con una tabla que una unidad adicional de X no provoca siempre el mismo cambio en \(p\).

Ejemplo conceptual:

| Horas iniciales | Probabilidad inicial | Probabilidad +1 hora | Cambio |
|---:|---:|---:|---:|
| 1 | baja | algo mayor | pequeño |
| 4 | intermedia | bastante mayor | grande |
| 8 | alta | ligeramente mayor | pequeño |

### Idea

Los efectos son mayores alrededor de la región central de la sigmoide y menores en sus extremos.

---

# MÓDULO 11 — De probabilidades a clases

El modelo devuelve:

\[
P(Y=1|X)
\]

pero finalmente necesitamos decidir entre:

\[
0 \quad \text{o} \quad 1
\]

Para ello definimos un **umbral**.

Por defecto suele utilizarse:

\[
t=0.5
\]

Regla:

\[
\hat Y =
\begin{cases}
1 & p\ge t\\
0 & p<t
\end{cases}
\]

---

# MÓDULO 12 — Umbral, falsos positivos y falsos negativos

Modificar gráficamente:

- \(t=0.2\)
- \(t=0.5\)
- \(t=0.8\)

## Umbral bajo

Clasificamos más casos como positivos.

Tienden a:

- aumentar verdaderos positivos;
- aumentar falsos positivos;
- disminuir falsos negativos.

## Umbral alto

Somos más exigentes para declarar un positivo.

Tienden a:

- disminuir falsos positivos;
- aumentar falsos negativos.

### Idea central

> El umbral no es necesariamente una verdad matemática. Es también una decisión asociada al problema.

Depende del costo relativo de:

- falso positivo;
- falso negativo.

### Ejemplo médico — usar con cuidado

En un sistema de *screening*, puede interesar reducir falsos negativos.

Un resultado positivo no implica comenzar directamente un tratamiento, sino normalmente realizar **estudios diagnósticos adicionales**.

---

# MÓDULO 13 — Caso práctico: riesgo crediticio

Segundo notebook.

Objetivo:

> Predecir si un cliente será buen o mal pagador.

Variable objetivo:

\[
Y=
\begin{cases}
1 & \text{mal pagador}\\
0 & \text{buen pagador}
\end{cases}
\]

Datos:

aproximadamente 9.700 observaciones y distintas características personales/económicas.

Ejemplos:

- género;
- vehículo;
- inmueble;
- hijos;
- ingreso;
- situación laboral;
- educación;
- estado civil;
- vivienda;
- antigüedad laboral;
- edad.

---

# MÓDULO 14 — Exploración y limpieza

Revisar:

```python
df.info()
```

y estructura general.

Eliminar variables sin interés predictivo o excesivamente incompletas.

Ejemplos utilizados:

- ID;
- teléfono;
- variables con demasiados `NA`.

Realizar algunas transformaciones:

- días de nacimiento → edad;
- días trabajados → años trabajados;
- situación laboral;
- transformación de indicadores 0/1 → categorías cuando sea útil para mostrar el proceso.

---

# MÓDULO 15 — Variables numéricas y categóricas

Explicar que los modelos requieren tratamientos diferentes.

### Numéricas

Ejemplos:

- edad;
- ingreso;
- cantidad de hijos;
- años trabajados.

### Categóricas

Ejemplos:

- género;
- estado civil;
- tipo de vivienda;
- tipo de trabajo.

Utilizar `make_column_selector` para identificar columnas.

---

# MÓDULO 16 — One Hot Encoding

Una variable categórica no puede ingresarse directamente como texto al modelo.

Ejemplo:

```text
Situación laboral

Empleado
Desempleado
```

One Hot Encoding produce indicadores:

```text
Empleado   Desempleado
1          0
0          1
```

Para más categorías, genera una columna por categoría.

Herramienta:

```python
OneHotEncoder()
```

---

# MÓDULO 17 — Estandarización

Para variables numéricas utilizar:

```python
StandardScaler()
```

Transformación:

\[
z=\frac{x-\bar x}{s}
\]

Resultado aproximado:

- media = 0;
- desviación estándar = 1.

### ¿Por qué?

Porque variables como:

- ingreso anual;

pueden trabajar en escalas completamente diferentes de:

- cantidad de hijos;
- antigüedad;
- edad.

---

# MÓDULO 18 — Train / Test

Separar los datos en:

- entrenamiento;
- prueba.

```python
train_test_split()
```

Ejemplo:

- 70 % entrenamiento;
- 30 % test.

### Corrección importante para próxima clase

**Dividir train/test antes de ajustar transformaciones.**

No estimar `StandardScaler` ni transformaciones aprendidas utilizando toda la muestra.

El flujo correcto es:

```text
Datos
  ↓
Train / Test
  ↓
Ajustar preprocessing SOLO con Train
  ↓
Entrenar modelo
  ↓
Aplicar transformaciones al Test
  ↓
Evaluar
```

La forma más segura es utilizar un `Pipeline`.

---

# MÓDULO 19 — Pipeline

Introducir la idea de tubería:

```text
Datos crudos
    ↓
Preprocesamiento
    ↓
Codificación
    ↓
Escalado
    ↓
Modelo
    ↓
Predicción
```

Ventajas:

- evita repetir código;
- reduce errores;
- mejora reproducibilidad;
- evita *data leakage*;
- permite aplicar exactamente las mismas transformaciones a train y test.

Idealmente utilizar:

```python
ColumnTransformer
```

+

```python
Pipeline
```

---

# MÓDULO 20 — Ajustar regresión logística

Modelo:

```python
LogisticRegression(max_iter=500)
```

Ajustar:

```python
modelo.fit(X_train, y_train)
```

Predecir:

```python
y_pred = modelo.predict(X_test)
```

Probabilidades:

```python
y_prob = modelo.predict_proba(X_test)
```

---

# MÓDULO 21 — Primera evaluación: Accuracy

Mostrar:

```python
modelo.score(X_test, y_test)
```

Resultado obtenido aproximadamente:

\[
Accuracy \approx 0.86
\]

Detener la clase acá.

### Pregunta

> Tenemos 86 % de accuracy. ¿Es un buen modelo?

**NO responder inmediatamente.**

Dejar la duda.

---

# MÓDULO 22 — La trampa del 86 %

Primero revisar:

```python
y.value_counts(normalize=True)
```

Si el conjunto está muy desbalanceado, un modelo trivial podría obtener una accuracy elevada simplemente prediciendo siempre la clase mayoritaria.

### Baseline

Calcular:

\[
Accuracy_{baseline}
=
\max[P(Y=0),P(Y=1)]
\]

Pregunta:

> ¿Cuánto mejora realmente nuestro modelo respecto de alguien que siempre dice “buen pagador”?

Esta es la transición a evaluación de clasificadores.

---

# MÓDULO 23 — Matriz de confusión

Introducir:

|  | Predicho 0 | Predicho 1 |
|---|---:|---:|
| **Real 0** | TN | FP |
| **Real 1** | FN | TP |

En nuestro problema:

**Clase 1 = mal pagador.**

Entonces interesa especialmente analizar:

### Falso negativo

Cliente realmente mal pagador que el modelo clasificó como buen pagador.

### Falso positivo

Cliente realmente buen pagador que clasificamos como riesgoso.

### Pregunta

> Para un banco, ¿tienen el mismo costo estos dos errores?

Conectar inmediatamente con el módulo anterior de **threshold**.

---

# MÓDULO 24 — Precision y Recall

Para la clase positiva:

### Precision

\[
Precision=
\frac{TP}{TP+FP}
\]

Pregunta que responde:

> De los clientes que marqué como malos pagadores, ¿cuántos realmente lo eran?

### Recall

\[
Recall=
\frac{TP}{TP+FN}
\]

Pregunta:

> De todos los malos pagadores reales, ¿cuántos logré detectar?

En riesgo crediticio puede ser especialmente importante entender el recall de la clase riesgosa.

No existe una métrica universalmente correcta: depende del costo del error.

---

# MÓDULO 25 — Threshold nuevamente

Ahora volver al concepto inicial.

El modelo produce probabilidades.

```python
modelo.predict_proba(X_test)
```

Podemos decidir:

```python
threshold = 0.30
```

en lugar de:

```python
threshold = 0.50
```

Modificar el threshold produce un trade-off:

```text
Threshold ↓
    ↓
Más positivos
    ↓
Recall ↑
Precision puede ↓
```

y viceversa.

La elección debe relacionarse con el problema económico o de negocios.

---

# MÓDULO 26 — Interpretación de coeficientes

Extraer:

```python
modelo.coef_
```

Asociarlos con los nombres de variables.

Ordenar por valor absoluto para inspeccionar cuáles tienen mayor peso dentro del modelo.

### Precaución

No interpretar automáticamente:

> coeficiente más grande = variable causalmente más importante.

Los coeficientes describen la relación del modelo, condicionada por:

- escala;
- demás variables;
- codificación;
- regularización;
- correlaciones.

---

# MÓDULO 27 — Variables dummy y categoría de referencia

Con una variable binaria:

```text
Empleado
Desempleado
```

One Hot Encoder puede generar:

```text
empleado
desempleado
```

pero ambas contienen esencialmente la misma información.

Si:

\[
Empleado=1
\]

entonces:

\[
Desempleado=0
\]

y viceversa.

Para una interpretación clásica más limpia, eliminar una categoría de referencia:

```python
OneHotEncoder(drop="first")
```

En variables con \(k\) categorías se utilizan normalmente:

\[
k-1
\]

indicadores.

### Nota técnica

Con modelos regularizados de `scikit-learn`, conservar todas las categorías no necesariamente impide estimar el modelo.

Sin embargo:

- introduce redundancia;
- dificulta la interpretación;
- cambia la parametrización de la regularización.

Para explicar coeficientes conviene trabajar con una categoría de referencia.

---

# MÓDULO 28 — Regularización en LogisticRegression

Recordar:

`LogisticRegression` de `scikit-learn` incorpora regularización por defecto.

Parámetro:

```python
C
```

Relación inversa:

```text
C grande
→ menor regularización

C pequeño
→ mayor regularización
```

Para aproximarse a una regresión logística sin penalización se puede utilizar la opción apropiada según la versión de `scikit-learn`.

**Revisar sintaxis antes de la clase**, porque ha cambiado entre versiones.

---

# CIERRE — Ideas que deberían llevarse

1. Clasificación no significa solamente generar 0 y 1.

2. La regresión logística primero estima:

\[
P(Y=1|X)
\]

3. La función logística convierte un predictor lineal en una probabilidad.

4. Los coeficientes son lineales en **log-odds**, no en probabilidades.

5. El threshold transforma probabilidades en decisiones.

6. Cambiar el threshold modifica falsos positivos y falsos negativos.

7. Accuracy puede ser muy engañosa con clases desbalanceadas.

8. La matriz de confusión permite entender **cómo** se está equivocando el modelo.

9. La métrica relevante depende del problema.

10. Un buen proyecto de Machine Learning incluye no solamente el modelo, sino también:

```text
datos
→ procesamiento
→ entrenamiento
→ evaluación
→ interpretación
→ decisión
```

---

# Guion sugerido de tiempos para próxima edición

| Módulo | Tiempo |
|---|---:|
| Anaconda + GitHub + entorno | 15–20 min |
| Introducción a clasificación | 10 min |
| Regresión logística + sigmoide | 20 min |
| Odds + interpretación | 15 min |
| Threshold + errores | 15 min |
| Caso crediticio + preprocessing | 25 min |
| Pipeline + modelo | 15 min |
| Accuracy + desbalance | 15 min |
| Matriz de confusión + métricas | 20 min |
| Discusión / cierre | 10 min |

---

# Preguntas para activar la clase

Evitar preguntas excesivamente abiertas como:

> “¿Qué opinan?”

Usar preguntas progresivas.

### Sigmoide

> Si \(\beta_1>0\), ¿la probabilidad aumenta o disminuye?

> ¿Aumenta siempre la misma cantidad?

### Threshold

> Si bajo el umbral de 0.5 a 0.2, ¿voy a clasificar más o menos observaciones como positivas?

> ¿Qué error debería aumentar?

### Accuracy

> 86 %. ¿Les parece mucho?

Luego:

> ¿Qué necesitan saber antes de responder?

### Desbalance

> Si el 87 % de los clientes son buenos pagadores, ¿qué accuracy obtiene un modelo que predice siempre “buen pagador”?

### Matriz de confusión

> Si ustedes fueran el banco, ¿qué les preocupa más: prestar a alguien que no paga o rechazar a alguien que sí habría pagado?

---

# Pendientes antes de volver a dar la clase

- [ ] Probar previamente Anaconda con una cuenta nueva.
- [ ] Revisar versión de `scikit-learn`.
- [ ] Revisar `OneHotEncoder(sparse_output=False)` según versión.
- [ ] Evitar mostrar Binder si no está funcionando.
- [ ] Preparar `Pipeline + ColumnTransformer`.
- [ ] Corregir preprocessing para evitar data leakage.
- [ ] Tener lista la distribución de la variable objetivo.
- [ ] Tener calculado el baseline de clase mayoritaria.
- [ ] Preparar matriz de confusión.
- [ ] Preparar precision y recall.
- [ ] Preparar ejemplo de cambio de threshold.
- [ ] Revisar interpretación de odds y \(e^\beta\).
- [ ] Mantener Anaconda/GitHub en máximo 20 minutos.

---

# Archivos de la clase

## Notebook 1 — Teórico

**Regresión logística**

Contiene:

- datos simulados;
- horas de estudio;
- comparación lineal vs logística;
- sigmoide;
- modificación de \(\beta_0\) y \(\beta_1\);
- odds;
- efectos sobre probabilidades;
- threshold;
- falsos positivos / falsos negativos.

## Notebook 2 — Práctico

**Regresión logística — Credit Scoring**

Contiene:

- carga de datos;
- limpieza;
- transformación;
- variables numéricas y categóricas;
- One Hot Encoding;
- StandardScaler;
- train/test;
- LogisticRegression;
- Pipeline;
- accuracy;
- interpretación de coeficientes;
- categorías de referencia;
- continuación: desbalance y matriz de confusión.

---

# Nota personal para la próxima clase

El hilo conductor debe ser:

> **Probabilidad → decisión → error → costo del error.**

No intentar enseñar todas las posibilidades de Python durante la misma clase.

Anaconda sirve para mostrar una forma profesional de organizar el trabajo, pero el núcleo de la clase sigue siendo:

> **cómo construir, interpretar y evaluar un clasificador.**