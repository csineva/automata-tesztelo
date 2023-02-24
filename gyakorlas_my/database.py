"""
This module simulates the database of the CommandLine Shop
"""

# Termékek - azonosító: int, név: str, ár: float
DATA = [
    [1, 'Alma', 100.0],
    [2, 'Körte', 150.5],
    [3, 'Répa', 50.0],
    [4, 'Saláta', 185.0],
    [5, 'Kolbász', 250.5],
    [6, 'Zsemle', 15.0]
]


def get_all_item() -> list:
    items = []
    for item in DATA:
        items.append(item)
    return items


def get_item_by_id(item_id: int) -> list:
    for i, item in enumerate(DATA):
        if int(item_id) == item[0]:
            return DATA[i]


def get_item_by_name(item_id: str) -> list:
    for i, item in enumerate(DATA):
        if item_id.lower() in item[1].lower():
            return DATA[i]


def add_new(item: list) -> bool:

    if len(item) != 2:
        return False
    for i in DATA:
        if i[1].lower() == item[0].lower():
            return False
    DATA.append([len(DATA)+1] + item)
    return True


def remove_item_by_(item_id: int) -> bool:
    item_exists = False
    for i, item in enumerate(DATA):
        if int(item_id) == item[0]:
            DATA.pop(i)
            item_exists = True
    return item_exists


def update_item(item: list) -> bool:
    pass