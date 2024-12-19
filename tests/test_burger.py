'''Тесты атрибутов и методов класса «Burger».'''
import pytest

from data import RECEIPT_TEMPLATE
from praktikum.burger import Burger


class TestBurger:

    @pytest.fixture(autouse=True)
    def create_burger_object(self):
        '''Создание нового объекта класса «Burger» для каждого теста.'''
        self.burger = Burger()

    def set_burger_attrs(self, *ingredients, bun=None):
        '''Передача бургеру булочки и ингредиентов.'''
        self.burger.bun = bun
        self.burger.ingredients = list(ingredients)

    def test_init_attr_bun_is_none(self):
        '''Атрибут «bun» по умолчанию - None.'''
        assert self.burger.bun is None

    def test_init_attr_ingredients_is_empty_list(self):
        '''Атрибут «ingredients» по умолчанию - пустой список.'''
        assert self.burger.ingredients == []

    def test_set_buns_attr_bun_takes_bun(self, mock_bun):
        '''Задать булку бургеру.'''
        self.burger.set_buns(mock_bun)
        assert self.burger.bun == mock_bun

    def test_add_ingredient_appends_ingredient(self, mock_ingredient):
        '''Добавление ингредиента бургеру.'''
        self.burger.add_ingredient(mock_ingredient)
        assert self.burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_deletes_ingredient(self, mock_ingredient):
        '''Удаление ингредиента бургера.'''
        self.set_burger_attrs(mock_ingredient)
        self.burger.remove_ingredient(index=0)
        assert self.burger.ingredients == []

    def test_move_ingredient_relocates_ingredient(self, mock_ingredient):
        '''Перемещение ингредиента бургера.'''
        self.set_burger_attrs('ingredient', mock_ingredient)
        self.burger.move_ingredient(index=1, new_index=0)
        assert self.burger.ingredients == [mock_ingredient, 'ingredient']

    def test_get_price_returns_burger_price(self, mock_bun, mock_ingredient):
        '''Получение цены бургера.'''
        self.set_burger_attrs(mock_ingredient, bun=mock_bun)
        expected = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        assert self.burger.get_price() == expected

    def test_get_receipt_returns_burger_receipt(
        self, mock_bun, mock_ingredient
    ):
        '''Получение рецепта бургера.'''
        self.set_burger_attrs(mock_ingredient, bun=mock_bun)
        data = {
            'bun_name': mock_bun.get_name(),
            'ingredient_type': mock_ingredient.get_type().lower(),
            'ingredient_name': mock_ingredient.get_name(),
            'price': mock_bun.get_price() * 2 + mock_ingredient.get_price()
        }
        assert self.burger.get_receipt() == RECEIPT_TEMPLATE.format(**data)
