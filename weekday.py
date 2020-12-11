#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This is weekday program

def main():

    weekday_string = input("Enter the number of weekday : ")
    print("")
    try:
        weekday_number = int(weekday_string)

        if weekday_number == 1:
            print("Monday")
        elif weekday_number == 2:
            print("Tuesday")
        elif weekday_number == 3:
            print("wednesday")
        elif weekday_number == 4:
            print("Thursday")
        elif weekday_number == 5:
            print("Friday")
        elif weekday_number == 6:
            print("Saturday")
        elif weekday_number == 7:
            print("Sunday")
        else:
            print("It is not number of month")
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
