import requests
from rest_framework import status

from core import settings
from core.settings import CUR_API_URL, CUR_API_KEY

import stripe


class Stripe_API:
    def __init__(self):
        self.stripe = stripe
        self.stripe.api_key = settings.STRIPE_API_KEY

    def get_products(self):
        return self.stripe.Product.list()

    def create_product(self, name, price):
        product = self.stripe.Product.create(name=name)
        return self.stripe.Price.create(
            currency="rub",
            unit_amount=price * 100,
            product=product.id,
        )

    def create_session(self, price_id):
        return self.stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[{"price": price_id, "quantity": 1}],
            mode="payment",
        )


def convert_price(rub_prise):
    response = requests.get(
        f'{CUR_API_URL}v3/latest?apikey={CUR_API_KEY}&currencies=RUB'
    )
    if response.status_code == status.HTTP_200_OK:
        rub_usd = response.json()['data']['RUB']['value']
        print(rub_usd)
        usd_prise = rub_prise * rub_usd
        return usd_prise
