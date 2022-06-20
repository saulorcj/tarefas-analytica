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


indicadores = ("PNT Geral", "PNT Mulheres negras", "PNT Mulheres responsáveis por domicílio menos 2 salários mínimos")
anos = (2019, )

for ano, indicador in zip(anos * 3, indicadores):
    print("ANO: {0}, INDICADOR: {1}".format(ano, indicador))
    media = get_media_proporcao(ano, indicador)
    print("media: {0:.2f}%".format(media))