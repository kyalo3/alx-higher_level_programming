#!/usr/bin/python3

def safe_print_integer_err(value):
    print_elements = 0
    x = print_elements
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]))
        except (ValueError, TypeError):
            pass
        else:
            print_elements += 1
    print()
    return (print_elements)
