import pandas as pd
dados = pd.read_csv("../datasets/proporcao_pessoas_proximas_pnt.csv")

regioes_brasil = {"Norte": {"PA"},
                  "Nordeste": {"CE", "PE", "BA"},
                  "Sudeste": {"MG", "RJ", "SP"},
                  "Centro-Oeste": {"DF"},
                  "Sul": {"PR"}}


def get_media_proporcao(ano, indicador):
    """
    :param ano: ano a ser selecionado
    :param indicador: indicador a ser selecionado
    :return: média da proporção de pessoas que moram perto de redes de transporte
    """
    media = dados[(dados["ano"] == ano) & (dados["indicador"] == indicador)]["prop_pessoas_proximas_pnt"].mean()
    return media


def get_media_proporcao_por_regiao(ano, indicador, regiao):

    media = dados[(dados["ano"] == ano) & (dados["indicador"] == indicador) &
                  (dados["sigla_uf"].isin(regioes_brasil[regiao]))]["prop_pessoas_proximas_pnt"].mean()
    return media


"""
Média dos indicadores gerais, de mulheres negras e de mulheres responsáveis por domicílio para o ano de 2019 
"""
indicadores = ("PNT Geral", "PNT Mulheres negras", "PNT Mulheres responsáveis por domicílio menos 2 salários mínimos")
anos = (2019, )
for ano, indicador in zip(anos * 3, indicadores):
    print("ANO: {0}, INDICADOR: {1}".format(ano, indicador))
    media = get_media_proporcao(ano, indicador)
    print("media: {0:.2f}%".format(media))
print("")
"""
Média dos indicadores gerais, de mulheres negras e de mulheres responsáveis por domicílio para o ano de 2019
nas regiões Sudeste e Nordeste
"""
regioes = ("Nordeste", "Sudeste")
for ano, indicador in zip(anos * 3, indicadores):
    for regiao in regioes:
        print("REGIÃO: {0}, ANO: {1}, INDICADOR: {2}".format(regiao, ano, indicador))
        media = get_media_proporcao_por_regiao(ano, indicador, regiao)
        print("media: {0:.2f}%".format(media))
