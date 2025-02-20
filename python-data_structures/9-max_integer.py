#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        if len(my_list) == 1:
            return my_list[0]
        else:
            int1 = my_list[0]
            int2 = max_integer(my_list[1:])

            if int1 > int2:
                return int1
            else:
                return int2
