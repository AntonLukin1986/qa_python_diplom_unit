from unittest.mock import Mock, patch

import pytest

from data import BUN, BUNS_DATA, INGREDIENT, INGREDIENT_DATA
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture(scope='session')
def mock():
    '''Создание объекта класса «Mock».'''
    return Mock()


@pytest.fixture(scope='session')
def mock_bun(mock):
    '''Создание мока класса «Bun».'''
    mock.configure_mock(**BUN)
    mock.get_name.return_value = mock.name
    mock.get_price.return_value = mock.price
    return mock


@pytest.fixture(scope='session')
def mock_ingredient(mock):
    '''Создание мока класса «Ingredient».'''
    mock.configure_mock(**INGREDIENT)
    mock.get_name.return_value = mock.name
    mock.get_price.return_value = mock.price
    mock.get_type.return_value = mock.type
    return mock


@pytest.fixture(scope='session')
def mock_buns_db(mock):
    '''Создание набора булок для заполнения БД.'''
    buns = []
    for name, price in BUNS_DATA:
        mock = Mock()
        mock.configure_mock(name=name, price=price)
        mock.get_name.return_value = mock.name
        mock.get_price.return_value = mock.price
        buns.append(mock)
    return buns


@pytest.fixture(scope='session')
def mock_ingredients_db():
    '''Создание набора ингредиентов для заполнения БД.'''
    ingredients = []
    for _type, name, price in INGREDIENT_DATA:
        mock = Mock()
        mock.configure_mock(type=_type, name=name, price=price)
        mock.get_type.return_value = mock.type
        mock.get_name.return_value = mock.name
        mock.get_price.return_value = mock.price
        ingredients.append(mock)
    return ingredients


@pytest.fixture(scope='session')
def test_bun():
    '''Создание объекта класса «Bun».'''
    return Bun(**BUN)


@pytest.fixture(scope='session')
def test_burger():
    '''Создание объекта класса «Burger».'''
    return Burger()


@pytest.fixture(scope='session')
def test_ingredient():
    '''Создание объекта класса «Ingredient».'''
    return Ingredient(**INGREDIENT)


@pytest.fixture(scope='session')
@patch('praktikum.database.Ingredient')
@patch('praktikum.database.Bun')
def test_database(
        mock_bun_init, mock_ingredient_init, mock_buns_db, mock_ingredients_db
   ):
    '''Создание объекта класса «Database».'''
    mock_bun_init.side_effect = mock_buns_db
    mock_ingredient_init.side_effect = mock_ingredients_db
    return Database()
