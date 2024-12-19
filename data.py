'''Статичные данные для тестов.'''
BUN = {'name': 'Булка', 'price': 10.5}
INGREDIENT = {'ingredient_type': 'Начинка', 'name': 'Гуакамоле', 'price': 20.0}
RECEIPT_TEMPLATE = (
    '(==== {bun_name} ====)\n= {ingredient_type} {ingredient_name} =\n'
    '(==== {bun_name} ====)\n\nPrice: {price}'
)
