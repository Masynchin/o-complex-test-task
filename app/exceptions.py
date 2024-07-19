class CityNotFound(Exception):
    """Город с таким названием не найден"""

    def __init__(self, city: str, *args):
        super().__init__(args)
        self.city = city


class EmptyHistory(Exception):
    ...
