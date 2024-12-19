from unittest.mock import Mock

import pytest

from data import BUN, INGREDIENT


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
