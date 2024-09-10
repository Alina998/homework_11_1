def filter_by_currency(transactions: list, currency_code: str):
    """Функция, которая возвращает итератор, выдающий транзакции с указанной валютой"""
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {}).get("currency", {}).get("code")
            == currency_code
        ):
            yield transaction


def transaction_descriptions(transactions: list):
    """Функция, которая поочередно возвращает описание каждой операции"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, end):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        # Форматируем номер карты, добавляя Leading zeros и разбивая на группы по 4 цифры
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[
            4:8
        ] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:]
