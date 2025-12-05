#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 1 and len(tuple_b) > 1:
        new_tuple = tuple(tuple_a[i] + tuple_b[i] for i in range(min(len(tuple_a), len(tuple_b))))
        return new_tuple
    else:
        pass
