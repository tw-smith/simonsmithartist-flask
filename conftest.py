import pytest
import stripe

@pytest.fixture(scope="function")
def get_test_price_object_gbp():
    price_gbp = {
      "id": "price_1MoBy5LkdIwHu7ixZhnattbh",
      "object": "price",
      "active": True,
      "billing_scheme": "per_unit",
      "created": 1679431181,
      "currency": "gbp",
      "custom_unit_amount": 1234,
      "livemode": False,
      "lookup_key": None,
      "metadata": {},
      "nickname": None,
      "product": "prod_NZKdYqrwEYx6iK",
      "recurring": {
        "aggregate_usage": None,
        "interval": "month",
        "interval_count": 1,
        "trial_period_days": None,
        "usage_type": "licensed"
      },
      "tax_behavior": "unspecified",
      "tiers_mode": None,
      "transform_quantity": None,
      "type": "recurring",
      "unit_amount": 1000,
      "unit_amount_decimal": "1000"
}
    yield price_gbp

@pytest.fixture(scope="function")
def get_test_price_object_usd():
    price_usd = {
      "id": "price_1MoBy5LkdIwHu7ixZhnattbh",
      "object": "price",
      "active": True,
      "billing_scheme": "per_unit",
      "created": 1679431181,
      "currency": "usd",
      "custom_unit_amount": 1234,
      "livemode": False,
      "lookup_key": None,
      "metadata": {},
      "nickname": None,
      "product": "prod_NZKdYqrwEYx6iK",
      "recurring": {
        "aggregate_usage": None,
        "interval": "month",
        "interval_count": 1,
        "trial_period_days": None,
        "usage_type": "licensed"
      },
      "tax_behavior": "unspecified",
      "tiers_mode": None,
      "transform_quantity": None,
      "type": "recurring",
      "unit_amount": 1000,
      "unit_amount_decimal": "1000"
}
    yield price_usd

@pytest.fixture(scope="function")
def get_test_price_object_eur():
    price_eur = {
      "id": "price_1MoBy5LkdIwHu7ixZhnattbh",
      "object": "price",
      "active": True,
      "billing_scheme": "per_unit",
      "created": 1679431181,
      "currency": "eur",
      "custom_unit_amount": 1234,
      "livemode": False,
      "lookup_key": None,
      "metadata": {},
      "nickname": None,
      "product": "prod_NZKdYqrwEYx6iK",
      "recurring": {
        "aggregate_usage": None,
        "interval": "month",
        "interval_count": 1,
        "trial_period_days": None,
        "usage_type": "licensed"
      },
      "tax_behavior": "unspecified",
      "tiers_mode": None,
      "transform_quantity": None,
      "type": "recurring",
      "unit_amount": 1000,
      "unit_amount_decimal": "1000"
}
    yield price_eur