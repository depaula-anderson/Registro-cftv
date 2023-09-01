import pandas as pd

registro = pd.read_csv('registro_31_08.csv')
tabela = pd.read_csv("descritivo.csv")

df_reg = pd.DataFrame(registro)
display(df_reg)

df_tab = pd.DataFrame(tabela)
display(df_tab)

tabela_final = df_reg.merge(df_tab, how="outer", left_on= 'CODIGO', right_on= 'CODIGO')
tabela_final.to_csv('tabela_final.csv')