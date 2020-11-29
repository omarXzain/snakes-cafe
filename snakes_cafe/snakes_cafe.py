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
    """
      )


meal = {}


def pickFood():
    order = ""
    while order != "quit":
        order = input('>')
        if order in meal:
            meal[order] += 1
        else:
            meal[order] = 1
        if order != "quit":
            print(
                f"** {meal[order]} order of {order} have been added to your meal")


if __name__ == '__main__':
    pickFood()
