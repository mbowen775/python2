# This is a sample Python script.

# Press Shift+10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    #Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}') # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    from random import random

    for i in range(5):
        print(random())

        from platform import platform

        print(platform())
        print(platform(1))
        print(platform(0, 1))


        def __hash__(self):
            if self.denominator == 1:
                # Get integers right.
                return hash(self.numerator)
            # Expensive check, but definitely correct.
            if self == float(self):
                return hash(float(self))
