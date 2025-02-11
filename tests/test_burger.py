'''Тесты атрибутов и методов класса «Burger».'''
from data import RECEIPT_TEMPLATE
from helpers import expected_burger_price, set_burger_attrs


class TestBurger:

    def test_init_attr_bun_is_none(self, test_burger):
        '''Атрибут «bun» по умолчанию - None.'''
        assert test_burger.bun is None

    def test_init_attr_ingredients_is_empty_list(self, test_burger):
        '''Атрибут «ingredients» по умолчанию - пустой список.'''
        assert test_burger.ingredients == []

    def test_set_buns_attr_bun_takes_bun(self, test_burger, mock_bun):
        '''Задать булку бургеру.'''
        test_burger.set_buns(mock_bun)
        assert test_burger.bun == mock_bun

    def test_add_ingredient_appends_ingredient(
            self, test_burger, mock_ingredient
       ):
        '''Добавление ингредиента бургеру.'''
        test_burger.add_ingredient(mock_ingredient)
        assert test_burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_deletes_ingredient(
            self, test_burger, mock_ingredient
       ):
        '''Удаление ингредиента бургера.'''
        test_burger = set_burger_attrs(test_burger, mock_ingredient)
        test_burger.remove_ingredient(index=0)
        assert test_burger.ingredients == []

    def test_move_ingredient_relocates_ingredient(
            self, test_burger, mock_ingredient
       ):
        '''Перемещение ингредиента бургера.'''
        test_burger = set_burger_attrs(
            test_burger, 'ingredient', mock_ingredient
        )
        test_burger.move_ingredient(index=1, new_index=0)
        assert test_burger.ingredients == [mock_ingredient, 'ingredient']

    def test_get_price_returns_burger_price(
            self, test_burger, mock_bun, mock_ingredient
       ):
        '''Получение цены бургера.'''
        test_burger = set_burger_attrs(
            test_burger, mock_ingredient, bun=mock_bun
        )
        assert (
            test_burger.get_price() ==
            expected_burger_price(mock_ingredient, bun=mock_bun)
        )

    def test_get_receipt_returns_burger_receipt(
            self, test_burger, mock_bun, mock_ingredient
       ):
        '''Получение рецепта бургера.'''
        test_burger = set_burger_attrs(
            test_burger, mock_ingredient, bun=mock_bun
        )
        data = {
            'bun_name': mock_bun.get_name(),
            'ingredient_type': mock_ingredient.get_type().lower(),
            'ingredient_name': mock_ingredient.get_name(),
            'price': expected_burger_price(mock_ingredient, bun=mock_bun)
        }
        assert test_burger.get_receipt() == RECEIPT_TEMPLATE.format(**data)
