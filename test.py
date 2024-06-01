lst = [1, [2, 3], [4, 5, [6, 7]]]

def lst_flatten(lst: list) -> list:
    lst1 = []
    for x in lst:
        if type(x) is int:
            lst1.append(x)
        else:
            lst1.extend(lst_flatten(x))
    return lst1

lst_flatten(lst)