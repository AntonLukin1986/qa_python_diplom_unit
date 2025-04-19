'''Статичные данные для тестов.'''
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
)

BUN = {'name': 'Булка', 'price': 10.5}
INGREDIENT = {'ingredient_type': 'Начинка', 'name': 'Гуакамоле', 'price': 20.0}

BUNS_DATA = [('black bun', 100), ('white bun', 200), ('red bun', 300)]
INGREDIENTS_DATA = [
    (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
    (INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
    (INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
    (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
    (INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
    (INGREDIENT_TYPE_FILLING, 'sausage', 300)
]

STR_BUN = '(==== {bun_name} ====)'
STR_INGREDIENT = '= {ingredient_type} {ingredient_name} ='
STR_PRICE = '\nPrice: {price}'
RECEIPT_TEMPLATE = '\n'.join([STR_BUN, STR_INGREDIENT, STR_BUN, STR_PRICE])
