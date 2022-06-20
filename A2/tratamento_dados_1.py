import pandas as pd

dados = pd.read_csv("../datasets/proporcao_pessoas_proximas_pnt.csv")

# Dados Gerais em 2019
dados_geral = dados[(dados["ano"] == 2019) & (dados["indicador"] == "PNT Geral")]
print(dados_geral.head())
media_proporcao_geral = dados_geral["prop_pessoas_proximas_pnt"].mean()
print("media de pessoas: {0:.2f}%".format(media_proporcao_geral))
"""
# Dados sobre mulheres negras em 2019
dados_mulh_negras = dados[dados["ano"] == 2019][dados["indicador"] == "PNT Mulheres negras"]
#print(dados_mulh_negras.head())
media_proporcao_mulh_negras = dados_mulh_negras["prop_pessoas_proximas_pnt"].mean()
print("media de mulheres negras: {0:.2f}%".format(media_proporcao_mulh_negras))

# Dados sobre mulheres responsáveis por domicílios menos 2 salários mínimos
dados_mulh_dom = dados[dados["ano"] == 2019][dados["indicador"] ==
                                             "PNT Mulheres responsáveis por domicílio menos 2 salários mínimos"]
print(dados_mulh_dom)
media_proporcao_mulh_dom = dados_mulh_dom["prop_pessoas_proximas_pnt"].mean()
print("media de mulheres responsáveis por domicílios: {0:.2f}%".format(media_proporcao_mulh_dom))
"""