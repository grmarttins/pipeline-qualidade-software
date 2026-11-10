import httpx
from datetime import date

URL_MOEDAS = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json"

def get_moedas() -> list[dict]:
    res = httpx.get(URL_MOEDAS)
    res.raise_for_status()
    dados = res.json()
    return dados["value"]


URL_COTACAO = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='{moeda}'&@dataCotacao='{data_atual}'&$top=100&$format=json"

def cotacao_atual(moeda: str, data_cotacao: date | None = None) -> list[dict]:
    if data_cotacao is None:
        data_cotacao = date.today()

    data_atual = data_cotacao.strftime("%m-%d-%Y")
    URL = URL_COTACAO.format(moeda=moeda, data_atual=data_atual)

    res = httpx.get(URL)
    res.raise_for_status()
    dados = res.json()
    return dados["value"]
    

if __name__ == "__main__":
    moedas = get_moedas()
    print(moedas)
    print("\n")
    # cotacao = cotacao_atual("USD", date(2026, 9,1))
    cotacao = cotacao_atual("USD")
    print(cotacao)