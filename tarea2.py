#### Tarea 2############
import pandas as pd
import numpy as np      
## Adquisicion de los datos####3
felicidad = pd.read_csv("https://raw.githubusercontent.com/cienciadedatos/datos-de-miercoles/master/datos/2019/2019-08-07/felicidad.csv")
felicidad
felicidad.info()
feli=felicidad.iloc[0:1704,0:3]
feli
#Primer anio a nivel global/ media y STD ###
df_filtrado = feli[feli['anio']==2008]
escalera_vida2008 = df_filtrado.iloc[0:1704,2]
escalera_vida1=pd.DataFrame(escalera_vida2008.describe() )
escalera_vida1
#####ultimo anio a nivel global/ media y STD#####
df_filtrado = feli[feli['anio']==2018]
escalera_vida2018 = df_filtrado.iloc[0:1704,2]
escalera_vida2018.describe() 
escalera_vida2 =pd.DataFrame(escalera_vida2018.describe() )
escalera_vida2
escalera_vida1.loc["mean"]
escalera_vida2.loc["mean"]
#crear un Dataframe de las medias gobales#################
glob1=({"pais":["global","global"],
 "escalera_vida":[5.418554,5.502134],
  "anio":[2008,2018]})
glob1t=pd.DataFrame(glob1 )
glob1t
## Nueva Zelanda##
feli
d_nueva = feli[feli['pais'].str.contains("Nueva Zelanda")]
d_nueva
df_filtrado_nueva2 = d_nueva[d_nueva['anio']==2008]
df_filtrado_nueva2
df_filtrado_nueva1= d_nueva[d_nueva['anio']==2018]
df_filtrado_nueva1
## mexico ##
d_mex = feli[feli['pais'].str.contains("México")]
d_mex
df_filtrado_mex1 = d_mex[d_mex['anio']==2008]
df_filtrado_mex1
df_filtrado_mex2= d_mex[d_mex['anio']==2018]
df_filtrado_mex2
### comparacion de los datos 
nueva_zelanda=pd.concat([df_filtrado_nueva2,df_filtrado_nueva1])
mexico =pd.concat([df_filtrado_mex1,df_filtrado_mex2])
mexico
######## comparacion a nivel global########
tot=pd.concat([nueva_zelanda,mexico])
tot
final=pd.concat([tot,glob1t])
final_tarea2= pd.DataFrame(final.set_index('pais'))
final_tarea2.reset_index(inplace=True)
final_tarea2
### Calidad_entrega ############
percepcion_corrupcion=felicidad.percepcion_corrupcion
feli["percepcion_corrupcion"]=percepcion_corrupcion
feli
d_nueva = feli[feli['pais'].str.contains("Nueva Zelanda")]
d_nueva
df_filtrado_nueva2 = d_nueva[d_nueva['anio']==2008]
df_filtrado_nueva2
df_filtrado_nueva1= d_nueva[d_nueva['anio']==2018]
df_filtrado_nueva1
d_mex = feli[feli['pais'].str.contains("México")]
d_mex
df_filtrado_mex1 = d_mex[d_mex['anio']==2008]
df_filtrado_mex1
df_filtrado_mex2= d_mex[d_mex['anio']==2018]
df_filtrado_mex2
## comparacion de los datos 
nueva_zelanda=pd.concat([df_filtrado_nueva2,df_filtrado_nueva1])
mexico =pd.concat([df_filtrado_mex1,df_filtrado_mex2])
tot=pd.concat([nueva_zelanda,mexico])
tot




