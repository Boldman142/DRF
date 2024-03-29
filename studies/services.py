import requests
from rest_framework import status

from core.settings import CUR_API_URL, CUR_API_KEY


def convert_price(rub_prise):
    response = requests.get(
        f'{CUR_API_URL}v3/latest?apikey={CUR_API_KEY}&currencies=RUB'
    )
    if response.status_code == status.HTTP_200_OK:
        rub_usd = response.json()['data']['RUB']['value']
        print(rub_usd)
        usd_prise = rub_prise * rub_usd
        return usd_prise
