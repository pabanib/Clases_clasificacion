import pandas as pd
import numpy as np
df = pd.read_csv("https://raw.githubusercontent.com/pabanib/dataframes/master/credit_card_completo.csv", index_col=0)
#df = pd.read_csv("credit_card_completo.csv", index_col=0)
df.to_csv("credit_card.csv")

df.rename(columns={'CODE_GENDER':'Genero',
                   'FLAG_OWN_CAR':'Auto',
                   'FLAG_OWN_REALTY':'Propiedad',
                   'CNT_CHILDREN':'Hijos',
                   'AMT_INCOME_TOTAL':'Ingreso_anual',
                   'NAME_EDUCATION_TYPE':'Nivel_educativo',
                   'NAME_FAMILY_STATUS':'Estado_civil',
                   'NAME_HOUSING_TYPE':'Vivienda',
                   'FLAG_EMAIL':'Email',
                   'FLAG_MOBIL':'Celular',
                   'DAYS_BIRTH':'Dias_nacimiento',
                   'DAYS_EMPLOYED':'Dias_empleado',
                   'NAME_INCOME_TYPE':'Tipo_trabajo',
                   'FLAG_WORK_PHONE':'Telefono_laboral',
                   'FLAG_PHONE':'Telefono_fijo',
                   'CNT_FAM_MEMBERS':'Tamaño_familia',
                   'OCCUPATION_TYPE':'Ocupacion',
                   'STATUS':'Calificacion'},
          inplace=True)
df.head(2)

df.drop(columns = ['ID','Celular','Ocupacion'], inplace=True)

df['Situacion_laboral'] = df.Dias_empleado.apply(lambda x: 'Desempleado' if x >= 0 else 'Empleado')
df['Años_empleado'] = df.Dias_empleado.apply(lambda x: round(-x/365.25, 2) if x < 0 else 0)
df['Edad'] = df.Dias_nacimiento.apply(lambda x: round(-x/365.25, 2))
df.drop(columns=["Dias_nacimiento","Dias_empleado"], inplace=True)
df.head()

df.replace({'Telefono_laboral':{1:'Y',0:'N'},
            'Telefono_fijo':{1:'Y',0:'N'},
            'Email':{1:'Y',0:'N'}},
           inplace=True)

df.Tamaño_familia = df.Tamaño_familia.astype(int)
df.to_csv('credit_card_procesado.csv')