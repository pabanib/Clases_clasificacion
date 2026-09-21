[[modelo_logit]]
El problema del modelo logit en scikit learn se va solucionar optimizando una función de costo. La función de costo tiene la lógica de lamáxima verosimilitud de una función binomial
$$
\min_{w}
\frac{1}{S}
\sum_{i=1}^{n}
s_i
\left(
-y_i \log\left(\hat{p}(X_i)\right)
-
(1-y_i)\log\left(1-\hat{p}(X_i)\right)
\right)
+
\frac{r(w)}{SC}
$$
donde:

$$
S = \sum_{i=1}^{n} s_i
$$
En este caso $s_i$  es el vector de pesos que asigna el usuario.

El término final de la suma modifica la fórmula clásica de máxima verosimilitud, esto se debe a que incorpora la regularización a los modelos logit. 

| Penalización                               | \(r(w)\)                                            |
| ------------------------------------------ | --------------------------------------------------- |
| Sin regularización (`C = np.inf`)          | \(0\)                                               |
| $\ell_1$ (`l1_ratio = 1`)                  | $(\lVert w \rVert_1)$                               |
| $\ell_2$ (`l1_ratio = 0`)                  | $\frac{1}{2}\lVert w \rVert_2^2 = \frac{1}{2}w^T w$ |
| Elastic Net (\(0 < \text{l1\_ratio} < 1\)) | $\frac{1-\rho}{2}w^T w + \rho \lVert w \rVert_1$    |

El parámetro $C$ controla inversamente la regularización por eso cuando este es infinito, hace que la regularización se convierta en ceroy por lo tanto tengamos la máxima versoimilitud