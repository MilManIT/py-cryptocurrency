from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy(get_exchange_rate_mock: int) -> None:
    get_exchange_rate_mock.return_value = 1.06
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell(get_exchange_rate_mock: int) -> None:
    get_exchange_rate_mock.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_if_0_95(get_exchange_rate_mock: int) -> None:
    get_exchange_rate_mock.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_if_1_05(get_exchange_rate_mock: int) -> None:
    get_exchange_rate_mock.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing"
