import pytest

from utils.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстура для создания тестовых данных
@pytest.fixture
def transactions_data():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 812345678,
            "state": "EXECUTED",
            "date": "2020-04-25T02:08:58.425572",
            "operationAmount": {
                "amount": "254.00",
                "currency": {"name": "EUR", "code": "EUR"},
            },
            "description": "Оплата налога",
            "from": "Счет 75106830613657916952",
            "to": "Счет 19708645243227258542",
        },
    ]


# Параметризованный тест
@pytest.mark.parametrize(
    "currency_code, expected_transactions",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
        (
            "EUR",
            [
                {
                    "id": 812345678,
                    "state": "EXECUTED",
                    "date": "2020-04-25T02:08:58.425572",
                    "operationAmount": {
                        "amount": "254.00",
                        "currency": {"name": "EUR", "code": "EUR"},
                    },
                    "description": "Оплата налога",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 19708645243227258542",
                }
            ],
        ),
        ("RUB", []),
    ],
)
def test_filter_by_currency(transactions_data, currency_code, expected_transactions):
    filtered_transactions = list(filter_by_currency(transactions_data, currency_code))
    assert filtered_transactions == expected_transactions


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 812345678,
                    "state": "EXECUTED",
                    "date": "2020-04-25T02:08:58.425572",
                    "operationAmount": {
                        "amount": "254.00",
                        "currency": {"name": "EUR", "code": "EUR"},
                    },
                    "description": "Оплата налога",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 19708645243227258542",
                },
            ],
            ["Перевод организации", "Перевод со счета на счет", "Оплата налога"],
        )
    ],
)
def test_transaction_descriptions(transactions, expected, transactions_data):
    # Вызываем функцию и преобразуем в список
    result = list(transaction_descriptions(transactions))
    assert result == expected


@pytest.fixture(
    params=[
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
        (
            0,
            3,
            [
                "0000 0000 0000 0000",
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
    ]
)
def range_data(request):
    return request.param


# Параметризованный тест для проверки генератора
def test_card_number_generator(range_data):
    start, end, expected_numbers = range_data
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected_numbers
