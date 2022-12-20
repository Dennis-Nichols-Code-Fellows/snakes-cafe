print(
    '''
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
    '''
)

order = {}
ordering = True
while ordering:
    item = input('> ')
    s = ''
    if item == 'quit':
        ordering = False
        break
    if item in order:
        order[item] += 1
        s = 's'
    else:
        order[item] = 1

    print(f"** {order[item]} order{s} of {item} have been added to your meal **")

print('''
****************
** Your Order **
****************
''')
for item in order:
    print(f"{item}: {order[item]}")

print('Thanks for visiting the Snakes Cafe!')
