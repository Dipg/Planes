import streamlit as st
import numpy as np
import operator
import pandas as pd
col1, col2,col3, col4 = st.beta_columns(4)


Servicios=["Guión","Modelos","VFX"]
Cantidades=[1,2,5]
Precios=[100,60,50]
Total = list(map(operator.mul, Cantidades, Precios))

pal=[]
palc=[]
palp=[]
with col1:
    st.markdown("**Incluye**")
    for i in Servicios :
        i=st.checkbox(i)
        pal.append(i)

with col2:
    st.markdown("**Cantidad**")
    for i in Cantidades :
        st.markdown(i)
        # palc.append(i)

with col3:
    st.markdown("**Precio**")
    for i in Precios :
        st.markdown(i)

df=pd.DataFrame({"check":pal,"Servicio":Servicios,"Cantidades":Cantidades,"Precios":Precios,"Total":Total})

df.loc[df["check"] == 0, ["Total"]] = 0

with col4:  
    col4.markdown("**Total**")
    for i in df["Total"]:
        st.markdown(i)  


st.markdown("# Total")
dfs=df.loc[df['check'] == 1]

suma=dfs["Total"].sum()

st.write("    #",suma)

dff=df.drop("check", axis=1)


