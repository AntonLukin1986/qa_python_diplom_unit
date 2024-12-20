'''Тесты атрибутов и методов класса «Database».'''
from unittest.mock import patch

import pytest

from data import BUNS_DATA, INGREDIENT_DATA
from praktikum.database import Database


class TestDatabase:

    @pytest.fixture(autouse=True)
    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def create_database_object(
        self, mock_bun_init, mock_ingredient_init,
        mock_buns_db, mock_ingredients_db
    ):
        '''Создание нового объекта класса «Database» для каждого теста.'''
        mock_bun_init.side_effect = mock_buns_db
        mock_ingredient_init.side_effect = mock_ingredients_db
        self.database = Database()

    def test_init_attr_buns_takes_list_of_buns(self):
        '''БД получает список булок при создании.'''
        buns = self.database.buns
        names_prices = [
            (bun.get_name(), bun.get_price()) for bun in buns
        ]
        assert isinstance(buns, list) and names_prices == BUNS_DATA

    def test_init_attr_ingredients_takes_list_of_ingredients(self):
        '''БД получает список ингредиентов при создании.'''
        ingredients = self.database.ingredients
        types_names_prices = [
            (ing.get_type(), ing.get_name(), ing.get_price())
            for ing in ingredients
        ]
        assert (
            isinstance(ingredients, list) and
            types_names_prices == INGREDIENT_DATA
        )

    def test_available_buns_returns_list_of_buns(self):
        '''Метод для получения доступных булок возвращает список булок.'''
        buns = self.database.available_buns()
        assert isinstance(buns, list) and buns == self.database.buns

    def test_available_ingredients_returns_list_of_ingredients(self):
        '''Метод для получения доступных ингредиентов возвращает список
        ингредиентов.'''
        ingredients = self.database.available_ingredients()
        assert (
            isinstance(ingredients, list) and
            ingredients == self.database.ingredients
        )
