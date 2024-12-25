'''Вспомогательные инструменты для тестов.'''


def expected_burger_price(*ingredients, bun):
    '''Рассчёт ожидаемой цены бургера.'''
    price = bun.get_price() * 2
    for ingredient in ingredients:
        price += ingredient.get_price()
    return price


def set_burger_attrs(burger, *ingredients, bun=None):
    '''Передача бургеру булочки и ингредиентов.'''
    burger.bun = bun
    burger.ingredients = list(ingredients)
    return burger
