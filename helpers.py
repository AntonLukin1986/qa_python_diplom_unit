'''Вспомогательные инструменты для тестов.'''


def expected_burger_price(*ingredients, bun):
    '''Расчёт ожидаемой цены бургера.'''
    price = bun.get_price() * 2
    for ingredient in ingredients:
        price += ingredient.get_price()
    return price


def set_burger_attrs(burger, *ingredients, bun=None):
    '''Передача бургеру булочки и ингредиентов.'''
    burger.bun = bun
    burger.ingredients = list(ingredients)
    return burger


def get_buns_data(buns):
    '''Получение характеристик булок.'''
    return [(bun.get_name(), bun.get_price()) for bun in buns]


def get_ingredients_data(ingredients):
    '''Получение характеристик ингредиентов.'''
    return [
        (ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
        for ingredient in ingredients
    ]
