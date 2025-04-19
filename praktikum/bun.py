class Bun:
    '''Модель булки для бургера. Булке можно дать название и назначить цену.'''

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        '''Получить название булки.'''
        return self.name

    def get_price(self) -> float:
        '''Получить цену булки.'''
        return self.price
