'''Тесты атрибутов и методов класса «Bun».'''
import pytest

from praktikum.bun import Bun

BUN = {'name': 'Булка', 'price': 10.5}


class TestBun:

    @pytest.fixture(autouse=True)
    def create_bun_object(self):
        '''Создание нового объекта класса «Bun» для каждого теста.'''
        self.bun = Bun(**BUN)               # нужно ли присваивание селф?
        return self.bun

    def test_init_bun_name_matches_passed_value(self):
        '''Название булки соответствует переданному значению и типу.'''
        name = self.bun.name
        assert isinstance(name, str) and name == BUN['name']            # как вариант собрать проверки в общий метод

    def test_init_bun_price_matches_passed_value(self):
        '''Цена булки соответствует переданному значению и типу.'''
        price = self.bun.price
        assert isinstance(price, float) and price == BUN['price']

    def test_get_name_returns_bun_name(self):
        '''Метод для получения названия возвращает название булки.'''
        name = self.bun.get_name()
        assert isinstance(name, str) and name == BUN['name']

    def test_get_price_returns_bun_price(self):
        '''Метод для получения цены возвращает цену булки.'''
        price = self.bun.get_price()
        assert isinstance(price, float) and price == BUN['price']
