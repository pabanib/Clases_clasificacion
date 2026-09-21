Las **odds** miden la relación entre la probabilidad de que ocurra un evento y la probabilidad de que no ocurra:

$$
\text{odds}=\frac{p}{1-p}
$$

Interpretación:

- Si $p=0.75$:

$$
\text{odds}=\frac{0.75}{0.25}=3
$$

Hay **3 casos favorables por cada 1 desfavorable**.

- Si $p=0.20$:

$$
\text{odds}=\frac{0.20}{0.80}=0.25
$$

Equivale a **1 caso favorable cada 4 desfavorables**.

### Traducción

Puede traducirse como **cociente de probabilidades a favor** o **razón de probabilidades**, aunque en textos técnicos suele mantenerse el término **odds**.

En regresión logística:

$$
\log\left(\frac{p}{1-p}\right)=X\beta
$$

El **logit** es el logaritmo de las odds.