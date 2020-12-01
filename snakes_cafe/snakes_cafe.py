print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
""")


meal = []

menu = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado',
        'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears']


def pickFood():
    order = ""

    while True:
        order = input('> ').capitalize()
        if order == 'quit':
            break

        if order in menu:
            meal.append(order)
            counter = meal.count(order)
            if order != "quit":
                print(
                    f"** {counter} order of {order} have been added to your meal")
        else:
            if order not in menu:
                print('Please choose from the menu above!')


if __name__ == '__main__':
    pickFood()
