import pandas as pd

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


ventas = pd.read_csv("https://raw.githubusercontent.com/pabanib/dataframes/master/online_retail.csv")
def procesos_generales():
    #country
    ventas['UK'] = ventas.Country.apply(lambda x: 1 if x == 'United Kingdom' else 0)
    #moda del producto, dummy por cada uno
    l = ventas.producto_mas_comprado.value_counts()[:4].index
    for p in l:
        ventas[p] = ventas.producto_mas_comprado.apply(lambda x: 1 if x == p else 0)

    ventas[l]

    #promedio de ventas
    ventas['gasto_prom_operacion'] = ventas.total_monto/ventas.cantidad_operaciones
    ventas['cant_prom_operacion'] = ventas.total_cantidades/ventas.cantidad_operaciones


    # Valores atipicos
    gpo_v_ext = ventas.gasto_prom_operacion.quantile([0.90]).values[0]
    cpo_v_ext = ventas.cant_prom_operacion.quantile([0.90]).values[0]

    ventas2 = ventas[(ventas.gasto_prom_operacion < gpo_v_ext) & (ventas.cant_prom_operacion < cpo_v_ext)]

    ventas2[['gasto_prom_operacion', 'cant_prom_operacion']].describe()

    #momento del día
    def momento_dia(hora):
        if hora < 6:
            return 'madrugada'
        elif hora < 12:
            return 'mañana'
        elif hora < 18:
            return 'tarde'
        else:
            return 'noche'

    ventas2['momento_dia'] = ventas2.hora_mas_frecuente.apply(momento_dia)

    return ventas2

numericas = ['gasto_prom_operacion', 'cant_prom_operacion','distintos_productos','cantidad_operaciones']
categoricas = ['momento_dia','UK',
       '84077 - WORLD WAR 2 GLIDERS ASSTD DESIGNS',
       '84879 - ASSORTED COLOUR BIRD ORNAMENT',
       '22492 - MINI PAINT SET VINTAGE ',
       '85123A - WHITE HANGING HEART T-LIGHT HOLDER']


preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numericas),
        ('cat', OneHotEncoder(drop='first'), categoricas)
    ]
)

def preprocesar():
    return preprocessor.fit_transform(procesos_generales())


########## 
### Información

import pandas as pd

def cuadro_variables():
    datos = [
        (
            "CustomerID",
            "Identificador único del cliente. Aunque aparece como número, se utiliza para identificarlo y no representa una cantidad.",
            "Categórica nominal — identificador."
        ),
        (
            "total_monto",
            "Importe total de las compras registradas para el cliente durante el período analizado. Representa su aporte a la facturación, no la ganancia que genera.",
            "Cuantitativa continua."
        ),
        (
            "total_cantidades",
            "Cantidad total de unidades compradas por el cliente. Incluye varias unidades de un mismo producto.",
            "Cuantitativa discreta."
        ),
        (
            "distintos_productos",
            "Cantidad de productos diferentes comprados por el cliente. Describe la variedad de su compra, independientemente de cuántas unidades adquirió de cada producto.",
            "Cuantitativa discreta."
        ),
        (
            "cantidad_operaciones",
            "Número de operaciones de compra registradas para el cliente durante el período analizado. Permite describir su frecuencia de compra.",
            "Cuantitativa discreta."
        ),
        (
            "hora_mas_frecuente",
            "Hora del día en la que el cliente registra compras con mayor frecuencia. Se expresa en formato de 24 horas y tiene un comportamiento cíclico: después de las 23 comienza nuevamente la hora 0.",
            "Temporal cíclica."
        ),
        (
            "repitio_mismo_dia",
            "Indicador de si el cliente realizó más de una operación de compra en una misma fecha. Toma el valor True cuando ocurrió y False cuando no ocurrió.",
            "Categórica binaria."
        ),
        (
            "producto_mas_comprado",
            "Producto identificado como el más comprado por el cliente. El campo contiene el código y la descripción del producto.",
            "Categórica nominal."
        ),
        (
            "Country",
            "País asociado al cliente en los registros de compra.",
            "Categórica nominal."
        ),
    ]

    return pd.DataFrame(
        datos,
        columns=["Columna", "Descripción", "Tipo de variable"]
    )

def informacion():
    with pd.option_context("display.max_colwidth", None):
        display(cuadro_variables())

