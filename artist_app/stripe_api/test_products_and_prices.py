from artist_app.stripe_api.products_and_prices import get_price_string


def test_get_price_string(get_test_price_object_gbp, get_test_price_object_usd, get_test_price_object_eur):
    price_string_gbp = get_price_string(get_test_price_object_gbp)
    price_string_eur = get_price_string(get_test_price_object_eur)
    price_string_usd = get_price_string(get_test_price_object_usd)

    assert price_string_gbp == '£12.34'
    assert price_string_eur == '€12.34'
    assert price_string_usd == '$12.34'

