list_tuple = []


def simple_sort(name, age, score):
    tuple_items = name, age, score
    list_tuple.append(tuple_items)
    list_tuple.sort()
    return list_tuple
