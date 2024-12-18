'''Тесты атрибутов и методов класса «Ingredient».'''
import pytest

from praktikum.ingredient import Ingredient

INGREDIENT = {'ingredient_type': 'начинка', 'name': 'Гуакамоле', 'price': 20.0}      # вынести


class TestIngredient:

    @pytest.fixture(autouse=True)
    def create_ingredient_object(self):
        '''Создание нового объекта класса «Ingredient» для каждого теста.'''
        self.ingredient = Ingredient(**INGREDIENT)               # нужно ли присваивание селф?
        return self.ingredient

    def test_init_ingredient_type_matches_passed_value(self):
        '''Тип ингредиента соответствует переданному значению и типу.'''
        _type = self.ingredient.type
        assert isinstance(_type, str) and _type == INGREDIENT['ingredient_type']            # как вариант собрать проверки в общий метод

    def test_init_ingredient_name_matches_passed_value(self):
        '''Название ингредиента соответствует переданному значению и типу.'''
        name = self.ingredient.name
        assert isinstance(name, str) and name == INGREDIENT['name']

    def test_init_ingredient_price_matches_passed_value(self):
        '''Цена ингредиента соответствует переданному значению и типу.'''
        price = self.ingredient.price
        assert isinstance(price, float) and price == INGREDIENT['price']

    def test_get_name_returns_ingredient_name(self):
        '''Метод для получения названия возвращает название ингредиента.'''
        name = self.ingredient.get_name()
        assert isinstance(name, str) and name == INGREDIENT['name']

    def test_get_price_returns_ingredient_price(self):
        '''Метод для получения цены возвращает цену ингредиента.'''
        price = self.ingredient.get_price()
        assert isinstance(price, float) and price == INGREDIENT['price']

    def test_get_type_returns_ingredient_type(self):
        '''Метод для получения типа возвращает тип ингредиента.'''
        _type = self.ingredient.get_type()
        assert isinstance(_type, str) and _type == INGREDIENT['ingredient_type']
