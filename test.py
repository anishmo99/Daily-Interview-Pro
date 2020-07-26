def split_list(n):
    """will return the list index"""
    return [(x+1) for x,y in zip(n, n[1:]) if y-x != 1]

def get_sub_list(my_list):
    """will split the list base on the index"""
    my_index = split_list(my_list)
    output = list()
    prev = 0
    for index in my_index:
        new_list = [ x for x in my_list[prev:] if x < index]
        output.append(new_list)
        prev += len(new_list)
    output.append([ x for x in my_list[prev:]])
    return output

# my_list = [1, 3, 4, 7, 8, 10, 11, 13, 14]
my_list = [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
print get_sub_list(my_list)