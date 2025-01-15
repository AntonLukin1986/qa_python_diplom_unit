'''Тесты атрибутов и методов класса «Bun».'''
from data import BUN


class TestBun:

    def test_init_bun_name_matches_passed_value(self, test_bun):
        '''Название булки соответствует переданному значению и типу.'''
        name = test_bun.name
        assert isinstance(name, str) and name == BUN['name']

    def test_init_bun_price_matches_passed_value(self, test_bun):
        '''Цена булки соответствует переданному значению и типу.'''
        price = test_bun.price
        assert isinstance(price, float) and price == BUN['price']

    def test_get_name_returns_bun_name(self, test_bun):
        '''Метод для получения названия возвращает название булки.'''
        name = test_bun.get_name()
        assert isinstance(name, str) and name == BUN['name']

    def test_get_price_returns_bun_price(self, test_bun):
        '''Метод для получения цены возвращает цену булки.'''
        price = test_bun.get_price()
        assert isinstance(price, float) and price == BUN['price']
