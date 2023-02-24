"""
This is the main module of the practice. Use this for running the application.
"""
from database import*
# SETTINGS -------------------------------------------------------------------------------------------------------------
CURRENT_ROLE = 'customer'

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    pass

print()
print('list items', '-' * 120)
print(get_all_item())

print()
print('list items by id', '-' * 120)
print(get_item_by_id(3))

print()
print('list items by name', '-' * 120)
print(get_item_by_name('a'))

print()
print('add', '-' * 120)
print(get_all_item())
print(add_new(['alma', 23]))
print(get_all_item())

print()
print('remove', '-' * 120)
print(get_all_item())
print(remove_item_by_(2))
print(get_all_item())
