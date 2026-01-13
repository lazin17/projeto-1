import pandas as pd 
df=pd.read_csv("dados_estudantes.csv")
print(df.head())
df.info()
df["turno"]=df["turno"].str.lower().str.strip()
df["escola"]=df["escola"].str.lower().str.strip()
df["idade"]=pd.to_numeric(df["idade"],errors="coerce")
df["nota"]=pd.to_numeric(df["nota"],errors="coerce")


df.info()
df_limpo=df.dropna(subset=["idade","nota"])
df_limpo.info()

media_por_turno=df_limpo.groupby("turno")["turno"].mean()
media_por_idade=df_limpo.groupby("turno")['idade'].mean()
melhor_turno=media_por_turno.idxmax()
print(f"turno com maior media:{melhor_turno}")
print("Media por idade :",media_por_idade)