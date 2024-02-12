#!/usr/bin/env python3

def binary_search(input_list, value):
    """ Sends the index position if a value is found or -1 if no match from a list of integers  """

    input_list.sort()
    left = 0
    right = len(input_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == value:
            return mid       
        if input_list[mid] < value:
            left = mid + 1
        elif input_list[mid] > value:
            right = mid - 1
    return -1                 

def main():
    numbers = input("Enter numbers separated by comma\n").split(",")
    value = int(input("Find the number "))
    numbers_int = list(map(int, numbers))
    print("Position is {}".format(binary_search(numbers_int, value)))

if __name__ == "__main__":
    main()
