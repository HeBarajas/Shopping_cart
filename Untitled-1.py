def target(shopping_cart = {}): #clear_output
    while True:
        
            ask_food = input('What would you like to add? ')
            ask_quantity = int(input(f'How many {ask_food} would you like to add? '))
            ask_price = float(input(f'How much does your {ask_food} cost? '))
            total_price = int(ask_quantity)*float(ask_price)
            shopping_cart[ask_food] = {'Quantity':ask_quantity}, {'Price': total_price}
    #-------------------------------Ask-Last Line-------------------------------------------------------------------------
            ask = input("What would you like to to do? Add/Show/Remove/Clear or Quit? ").lower()
            if ask == 'remove':
                ask_remove = input('which item would you like to remove? ').lower()
                ask_remove == shopping_cart.pop(ask_food)
            elif ask == 'add':
                continue
            elif ask == 'clear':
                dict.clear()
                continue 
            elif ask == 'show':

                print(f'{shopping_cart}')
                continue
            elif ask == 'quit':
                print(f'{shopping_cart}')
                break
                #clear_output()
target(shopping_cart = {})
