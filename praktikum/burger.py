from typing import List

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class Burger:
    '''Модель бургера.
    Бургер состоит из булок и ингредиентов (начинка или соус).
    Ингредиенты можно перемещать и удалять.
    Можно распечать чек с информацией о бургере.'''

    def __init__(self):
        self.bun = None
        self.ingredients: List[Ingredient] = []

    def set_buns(self, bun: Bun):
        '''Добавить булку.'''
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient):
        '''Добавить ингредиент.'''
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        '''Убрать ингредиент.'''
        del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        '''Переместить ингредиент.'''
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self) -> float:
        '''Получить цену.'''
        price = self.bun.get_price() * 2
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    def get_receipt(self) -> str:
        '''Получить рецепт.'''
        receipt: List[str] = [f'(==== {self.bun.get_name()} ====)']
        for ingredient in self.ingredients:
            receipt.append(
                f'= {ingredient.get_type().lower()} '
                f'{ingredient.get_name()} ='
            )
        receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        receipt.append(f'Price: {self.get_price()}')
        return '\n'.join(receipt)
