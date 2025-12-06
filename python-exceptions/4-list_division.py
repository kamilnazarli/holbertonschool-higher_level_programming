#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            temp = my_list_1[i] / my_list_2[i]
            res.append(temp)
        except TypeError:
            print("wrong type")
            res.append(0)
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
        except IndexError:
            print("out of range")
            res.append(0)
        finally:
            continue
    return res

