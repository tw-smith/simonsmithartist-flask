import pytest

import stripe
from artist_app import create_app
from config import TestConfig

test_price_id_eur = "price_1OPSeWDKpC50uLWTA6KTz4ZC"
test_price_id_usd = "price_1OPSijDKpC50uLWTBywD3inB"
test_price_id_gbp = "price_1OPSjLDKpC50uLWTk4XtZZqD"


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    yield app


@pytest.fixture(scope="function")
def get_test_price_object_gbp(app):
    stripe.api_key = app.config['STRIPE_SECRET_API_KEY_DEV']
    print(f"API KEY: {app.config['STRIPE_SECRET_API_KEY_DEV']}")
    yield stripe.Price.retrieve(test_price_id_gbp)


@pytest.fixture(scope="function")
def get_test_price_object_usd(app):
    stripe.api_key = app.config['STRIPE_SECRET_API_KEY_DEV']
    yield stripe.Price.retrieve(test_price_id_usd)


@pytest.fixture(scope="function")
def get_test_price_object_eur(app):
    stripe.api_key = app.config['STRIPE_SECRET_API_KEY_DEV']
    yield stripe.Price.retrieve(test_price_id_eur)
