import pandas as pd
df=pd.read_csv("dados_estudantes.csv")
df["turno"]=df["turno"].str.lower().str.strip()
df["nota"]=pd.to_numeric(df["nota"],errors="coerce")
def classificar_desempenho(nota):
    if nota>=7:
        return "bom"
    elif nota>=5:
        return "regular"
    else:
        return "baixo"

df["desempenho"]=df["nota"].apply(classificar_desempenho)
#print(df.head()

df=df.dropna(subset=["nota"])
destaques={}
for _,linha in df.iterrows():
    if linha["nota"]>=9:
        destaques[linha["id"]]=linha["nota"]

print(destaques)

media_por_turno={}
for  turno in df["turno"].unique():
    media=df[df["turno"]==turno]["nota"].mean()
    media_por_turno[turno]=media

print("Media por turno:",media_por_turno)

orcamento=20
while orcamento>0:
    orcamento-=5
    print("gastei 5 reais")