#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element of 2 lists

    Handles zero division error
    Handles wrong type error
    inequality in the length of the 2 list

    returns a new list containing all divisions
    """
    division_list = []
    for x in range(list_length):
        try:
            division_list.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            print("wrong type")
            division_list.append(0)

        except ZeroDivisionError:
            print("division by 0")
            division_list.append(0)

        except IndexError:
            print("out of range")
            division_list.append(0)

        finally:
            pass

    return (division_list)
