### Modelo Logit

El problema que tiene el modelo lineal para determinar una probabilidad, es que a menudo arroja valores negativos o valores mayores a 1, lo que no son valores que puedan identificarse como probabilidades. Para solucionar esto, se considera la función logística que devuelve todos valores entre 0 y 1.

$$
p\left(y = 1|\boldsymbol{X}=x\right)=p\left(\boldsymbol{X}\right) = \frac{e^{\boldsymbol{X}\boldsymbol{\beta}}}{1+e^{\boldsymbol{X}\boldsymbol{\beta}}}
$$

Si aplicamos transformaciones podemos ver que la ecuación nos queda de la siguiente forma:

$$
log\left(\frac{p\left(\boldsymbol{X}\right)}{1-p\left(\boldsymbol{X}\right)}\right) = \boldsymbol{X}\boldsymbol{\beta}
$$

la proporción $\frac{p\left(\boldsymbol{X}\right)}{1-p\left(\boldsymbol{X}\right)}$ se denomina *odds* [[Odds]], y puede tomar valores que van del 0 al $\infty$. Como podemos ver el modelo de regresión sigue siendo lineal en $\boldsymbol{X}$ pero con respecto al *log-odds* que es como se denomina a la parte de la izquierda de la ecuación anterior.

La forma de estimar este modelo es a través de máxima verosimilitud, en el cual no vamos a entrar en detalles acá.

Para realizar la estimación en R, se utiliza la función *glm*. La forma de uso es muy similar a *lm* necesita que le pasemos la fórmula a estimar y los datos necesarios como variables principales. Además se le agrega la variable *family* en la cual hay que colocarle que queremos estimar una *binomial*. Esta función en R es mucho más amplia que solo para estimar modelos logit, en realidad funcióna para estimar cualquier modelo lineal generalizado, lo que hay que variar es el parámetro *family*.