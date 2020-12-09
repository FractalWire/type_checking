from enum import IntEnum


class TasteRating(IntEnum):
    BAD = 1
    AVERAGE = 2
    GREAT = 3


class Fruit:
    def __init__(self, name: str, radius: int, taste_rating: int) -> None:
        self.radius: int = radius
        self.taste_rating: int = taste_rating
        self.name: str = name

    def good_bite(self) -> bool:
        return self.taste_rating > TasteRating.AVERAGE


class Apple(Fruit):
    # compatible python 2 notation
    def __init__(self, name, radius, taste_rating, color):
        # type: (str, int, int, str) -> None
        super().__init__(name, radius, taste_rating)
        self.color = color  # type: str

    # class type
    # def apple_to_apple(self, another_apple: Apple) -> Apple:
    def apple_to_apple(self, another_apple: 'Apple') -> 'Apple':
        gbs = self.good_bite()
        gba = another_apple.good_bite()
        if not (gba ^ gbs):
            if self.radius > another_apple.radius:
                return self
            return another_apple
        return self if gbs else another_apple

    # class from outside class
    def real_taste(self) -> TasteRating:
        return TasteRating(self.taste_rating)
