#!/usr/bin/env python3

def linear_search(numbers_int, value):
    """ Sends the index position if a value is found or -1 if no match from a list of integers  """
    
    for i, item in enumerate(numbers_int):
        if item == value:
            return i  	 
    return -1                        

def main():
    numbers = input("Enter numbers separated by comma\n").split(",")
    value = int(input("Find the number "))
    numbers_int = list(map(int, numbers))
    print("Position is {}".format(linear_search(numbers_int, value)))

if __name__ == "__main__":
    main()
