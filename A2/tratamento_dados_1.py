import pandas as pd
dados = pd.read_csv("../datasets/proporcao_pessoas_proximas_pnt.csv")


def get_media_proporcao(ano, indicador):
    """
    :param ano: ano a ser selcionado
    :param indicador: indicador a ser selecionado
    :return: média da proporção de pessoas que moram perto de redes de transporte
    """
    media = dados[(dados["ano"] == ano) & (dados["indicador"] == indicador)]["prop_pessoas_proximas_pnt"].mean()
    return media


# Dados Gerais em 2019
media_proporcao_geral = get_media_proporcao(2019, "PNT Geral")
print("media de pessoas: {0:.2f}%".format(media_proporcao_geral))

# Dados sobre mulheres negras em 2019
media_proporcao_mulh_negras = get_media_proporcao(2019, "PNT Mulheres negras")
print("media de mulheres negras: {0:.2f}%".format(media_proporcao_mulh_negras))

# Dados sobre mulheres responsáveis por domicílios menos 2 salários mínimos
media_proporcao_mulh_dom = get_media_proporcao(2019, "PNT Mulheres responsáveis por domicílio menos 2 salários mínimos")
print("media de mulheres responsáveis por domicílios: {0:.2f}%".format(media_proporcao_mulh_dom))