# Regresión logística con clases desbalanceadas

Cuando una clase aparece con mucha menor frecuencia que la otra, una regresión logística puede tender a clasificar casi todas las observaciones en la clase mayoritaria.

## 1. Ponderar las clases

Una solución directa es asignar mayor peso a los errores cometidos sobre la clase minoritaria.

En `scikit-learn`:

```python
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression(class_weight="balanced")