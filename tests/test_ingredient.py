'''Тесты атрибутов и методов класса «Ingredient».'''
from data import INGREDIENT


class TestIngredient:

    def test_init_ingredient_type_matches_passed_value(self, test_ingredient):
        '''Тип ингредиента соответствует переданному значению и типу.'''
        _type = test_ingredient.type
        assert (
            isinstance(_type, str) and _type == INGREDIENT['ingredient_type']
        )

    def test_init_ingredient_name_matches_passed_value(self, test_ingredient):
        '''Название ингредиента соответствует переданному значению и типу.'''
        name = test_ingredient.name
        assert isinstance(name, str) and name == INGREDIENT['name']

    def test_init_ingredient_price_matches_passed_value(self, test_ingredient):
        '''Цена ингредиента соответствует переданному значению и типу.'''
        price = test_ingredient.price
        assert isinstance(price, float) and price == INGREDIENT['price']

    def test_get_name_returns_ingredient_name(self, test_ingredient):
        '''Метод для получения названия возвращает название ингредиента.'''
        name = test_ingredient.get_name()
        assert isinstance(name, str) and name == INGREDIENT['name']

    def test_get_price_returns_ingredient_price(self, test_ingredient):
        '''Метод для получения цены возвращает цену ингредиента.'''
        price = test_ingredient.get_price()
        assert isinstance(price, float) and price == INGREDIENT['price']

    def test_get_type_returns_ingredient_type(self, test_ingredient):
        '''Метод для получения типа возвращает тип ингредиента.'''
        _type = test_ingredient.get_type()
        assert (
            isinstance(_type, str) and _type == INGREDIENT['ingredient_type']
        )
