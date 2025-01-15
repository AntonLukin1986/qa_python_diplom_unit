'''Тесты атрибутов и методов класса «Database».'''
from data import BUNS_DATA, INGREDIENT_DATA
from helpers import get_buns_data, get_ingredients_data


class TestDatabase:

    def test_init_attr_buns_takes_list_of_buns(self, test_database):
        '''БД получает список булок при создании.'''
        buns = test_database.buns
        assert isinstance(buns, list) and get_buns_data(buns) == BUNS_DATA

    def test_init_attr_ingredients_takes_list_of_ingredients(
            self, test_database
       ):
        '''БД получает список ингредиентов при создании.'''
        ingredients = test_database.ingredients
        assert (
            isinstance(ingredients, list) and
            get_ingredients_data(ingredients) == INGREDIENT_DATA
        )

    def test_available_buns_returns_list_of_buns(self, test_database):
        '''Метод для получения доступных булок возвращает список булок.'''
        buns = test_database.available_buns()
        assert isinstance(buns, list) and buns == test_database.buns

    def test_available_ingredients_returns_list_of_ingredients(
            self, test_database
       ):
        '''Метод для получения доступных ингредиентов возвращает список
        ингредиентов.'''
        ingredients = test_database.available_ingredients()
        assert (
            isinstance(ingredients, list) and
            ingredients == test_database.ingredients
        )
