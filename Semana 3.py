#######Dia1#############
mi_diccionario ={"nombre":"Denisse",
                "edad":36,
                "licencia":False}
mi_diccionario
mi_diccionario ={"nombre":"lissy",
                 "edad":24,
                 "deportes" : ["correr","bicicleta"]}
mi_diccionario
mi_diccionario1 = dict (nombre="lissy",
                        edad = 24,
                        licencia = False)
                        mi_diccionario.values()
mi_diccionario["edad"]=50                        
mi_diccionario.get("nombre")
mi_diccionario["educacion"]="universidad"
mi_diccionario
for llave in mi_diccionario:
   print(llave)
for llave in mi_diccionario:
    print(mi_diccionario[llave])
for llave in mi_diccionario:
    if llave =="edad":
        print(llave,mi_diccionario[llave])
clase={"estudiante":{"nombre":"Denisse","edad":24},
        "estudiante2":{"nombre":"Gerardo","edad":36}}
clase["estudiante2"]["nombre"]
clase["estudiante"]["nombre"]
import pandas as pd
import numpy as np
midic=({"nombres":["Denisse","Gerado","Angie"],
 "edades":[36,16,25]})
pd.DataFrame(midic)
midic["educacion"]=["universidad","preparatoria",np.nan]
midic
pd.DataFrame(midic)
mi_df=pd.DataFrame(midic)
mi_df
mi_df["educacion"].isnull()
mi_df["nombres"][1]
mi_df.iloc[1:3,0:2]
mi_df.iloc[1:2,0:2]
mi_df.iloc[1:2,1:3]
##########Dia2###########
import numpy as np
{nombre = "lissy","livia","milka","edades"=[19.25,36], educacion}
datos = pd.read_csv("https://raw.githubusercontent.com/laboratoriolide/new-dimensions/main/Python/prueba2.csv")
datos
array= np.loadtxt("prueba.csv",delimiter=",")
array
datos_pb=pd.read_csv("https://raw.githubusercontent.com/swcarpentry/python-novice-gapminder/main/episodes/data/gapminder_gdp_americas.csv",index_col= "country")
datos_pb.loc["Uraguay":"Venezuela"]
datos_pb["continent"]
datos_pb=pd.read_csv("https://raw.githubusercontent.com/swcarpentry/python-novice-gapminder/main/episodes/data/gapminder_gdp_americas.csv")
datos_pb.iloc[19:25]
datos_pb.columns
for col in datos_pb.columns:
  if "1967" in col:
      print(datos_pb[col])
col
datos_pb.describe()  
datos_pb.head()
datos_pb.tail()
datos_pb.T
datos_pb.info()
datos_pb["country"]
datos_pb.country
datos_pb[datos_pb["country"]=="Ecuador"]
###### 3 dia #######
import glob
import os
os.getcwd()
glob.glob("python/*.csv")
glob.glob("*/*.csv")
glob.glob("python/gapminder_all.csv")
archivos_pib= glob.glob("*/*gdp*.csv")
archivos_pib
pd.read_csv(archivos_pib[0])
mi_lista=[]
for archivo in archivos_pib:
  datos=pd.read_csv(archivo)
  mi_lista.append(datos)
len(mi_lista)
pib_mundo= pd.concat((mi_lista))
pib_mundo.head(n=3)
pib_mundo[~pib_mundo.continent.isnull()]
pib_mundo.loc[pib_mundo.continent.isnull(),"continent"]="Otros"
pib_mundo
pib_mundo.groupby("continent")["gdpPercap_1952"].mean()
for archivos in archivos_pib:
  datos=pd.read_csv(archivos)
pib_africa= pd.read_csv(archivos_pib[0])  
pib_africa
pib_africa= pd.read_csv(archivos_pib[0])
pib_asia= pd.read_csv(archivos_pib[2])
pib_africa.shape[0]+pib_asia.shape[0]
pd.concat([pib_africa,pib_asia])
carpeta_final="datosprocesados"
os.makedirs("datosprocesados",exist_ok=True)
os.makedirs("carpeta_final",exist_ok=True)
os.path.join(carpeta_final,"pib_mundo.csv")
pib_mundo.to_csv(os.path.join(carpeta_final,"pib_mundo.csv"))
###### 4 dia #######
import pandas as pd
datos1= pd.read_csv("python/gapminder_all.csv")
datos1
pob_cont_2007= datos1.groupby("continent")["pop_2007"].sum()
type(pob_cont_2007)
pob_cont_2007= pd.DataFrame(pob_cont_2007)
pob_cont_2007.iloc[2]
pob_cont_2007.index
pob_cont_2007= pob_cont_2007.reset_index(inplace=True)
pb_1952= datos1.iloc[:,0:3]
pb_1952
pb_1952["pib_por_mil"]= pb_1952.apply(lambda x:x["gdpPercap_1952"]*1000,axis=1)
#datos.loc[]
columnas = datos1.columns.tolist()
columnas
poblacion=[]
for i in columnas:
  if i.startswith("pop"):
    poblacion.append(i)
poblacion.append("country")
datos2=datos1[poblacion]
datos2
import matplotlib.pyplot as plt
datos2["pop_1952"].plot()
plt.show()
datos2[datos2.country == "Ecuador"].plot(kind="bar")
plt.show()
