from typing import Dict, TYPE_CHECKING

from fruits import Apple

if TYPE_CHECKING:
    from fruits import TasteRating


def get_some_taste(apple: Apple) -> 'TasteRating':
    return apple.real_taste()

# with python > 3.7
# from __future__ import annotations

# def get_some_taste(apple: Apple) -> TasteRating:
#     return apple.real_taste()


apple1 = Apple("golden", 1, 1, "yellow")
apple2 = Apple("granny", 2, 3, "green")
apple3 = Apple("Gala", 1, 2, "yellow")
# bad_apple = Apple("golden", 1, 1, 1)

# bad assign
# apple1.color = 1

# custom type
apple_dict_type = Dict[str, Apple]

apples: apple_dict_type = {
    apple1.name: apple1,
    apple2.name: apple2,
    apple3.name: apple3,
}

best_apple = apple1.apple_to_apple(apple2.apple_to_apple(apple3))

# implicit type
# best_apple = 1

print(best_apple.name, get_some_taste(best_apple))
