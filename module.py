"""
Mutation Challenge

These functions are supposed to return NEW data
without modifying the original input.

However, they currently contain mutation bugs.

Fix the functions so that the original data
is NOT changed.
"""


# -------------------------------------------------
# add_item
# -------------------------------------------------
# Takes a list and an item, and returns a NEW list
# with the item added to the end.
#
# The original list should NOT be modified.
#
# Example:
#   lst = [1, 2]
#   new_lst = add_item(lst, 3)
#   new_lst -> [1, 2, 3]
#   lst -> [1, 2]
#
def add_item(lst: list, item) -> list:
    lst.append(item)   # BUG: mutates original list
    return lst


# -------------------------------------------------
# remove_item
# -------------------------------------------------
# Takes a list and an item, and returns a NEW list
# with the first occurrence of the item removed.
#
# The original list should NOT be modified.
#
# Example:
#   lst = [1, 2, 3]
#   new_lst = remove_item(lst, 2)
#   new_lst -> [1, 3]
#   lst -> [1, 2, 3]
#
def remove_item(lst: list, item) -> list:
    lst.remove(item)   # BUG
    return lst


# -------------------------------------------------
# update_score
# -------------------------------------------------
# Takes a dictionary of scores, a name, and a new score.
# Returns a NEW dictionary with the updated score.
#
# The original dictionary should NOT be modified.
#
# Example:
#   scores = {"Alice": 90}
#   new_scores = update_score(scores, "Alice", 100)
#   new_scores -> {"Alice": 100}
#   scores -> {"Alice": 90}
#
def update_score(scores: dict, name: str, new_score: int) -> dict:
    scores[name] = new_score   # BUG
    return scores


# -------------------------------------------------
# append_to_tuple
# -------------------------------------------------
# Takes a list of tuples and a tuple, and returns a NEW list
# with the tuple added.
#
# The original list should NOT be modified.
#
# Example:
#   data = [(1, 2)]
#   new_data = append_to_tuple_list(data, (3, 4))
#   new_data -> [(1, 2), (3, 4)]
#   data -> [(1, 2)]
#
def append_to_tuple(data: tuple, item) -> tuple:
    data.append(item)   # BUG
    return data