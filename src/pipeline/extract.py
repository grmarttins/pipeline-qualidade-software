import httpx


URL_MOEDAS = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json"

def get_moedas() -> list[dict]:
    res = httpx.get(URL_MOEDAS)
    res.raise_for_status()
    dados = res.json()
    return dados["value"]

if __name__ == "__main__":
    moedas = get_moedas()
    print(moedas)