"""
Calculate the value of the change (coins) the user has.
"""
from tkinter import messagebox, simpledialog, Tk

# Write your code under the if __name__ == '__main__': below
def vending_machine(money):
    items_for_sale = {"water" : 0.50, "soda" : 1.00, "pretzels" : 1.00, "candy bar" : 1.50, "exit" : 0.00}

    while True:
        intro_str = "Welcome to the vending machine! You have " +\
                    str("{:.2f}".format(money)) + " dollars left.\n"
        intro_str += "Enter the item you want to buy?\n"

        for item, cost in items_for_sale.items():
            intro_str += item + ' - $' + str("{:.2f}".format(cost)) + '\n'

        item_num = simpledialog.askstring(title='Vending Machine', prompt=intro_str)

        # Cancel button pressed
        if item_num is None:
            return 0.00
        elif item_num in items_for_sale:
            return items_for_sale[item_num]
        else:
            messagebox.showwarning('Invalid item',
                                   'Please enter one of the following ' + str([item for item in items_for_sale]))


# ======================= DO NOT EDIT THE CODE ABOVE =========================


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    money_in_dollars = 3.00

    # TODO) Write a while loop that ends when you have no money left
    while money_in_dollars >= .01:
        money_spent = vending_machine(money_in_dollars)


        def vending_machine(money):
            items_for_sale = {"water": 0.50, "soda": 1.00, "pretzels": 1.00, "candy_bar": 1.50, "exit": 0.00}

            while True:
                intro_str = "Welcome to the vending machine! You have " + \
                            str("{:.2f}".format(money)) + " dollars left.\n"
                intro_str += "Enter the item you want to buy?\n"

                for item, cost in items_for_sale.items():
                    intro_str += item + ' - $' + str("{:.2f}".format(cost)) + '\n'
            item_num = simpledialog.askstring(title='Vending Machine', prompt=intro_str)
            if item_num is None:
                return 0.00
            elif item_num in items_for_sale:
                return items_for_sale[item_num]
            else:
                messagebox.showwarning('Invalid item',
                                       'Please enter one of the following ' + str([item for item in items_for_sale]))
            if item  == 'exit':
                messagebox.showinfo(None, "You still have " + str("{:.2f}".format(money)) + " left. ")
                item_num = False
            if item == 'water':
                money_in_dollars = int(money_in_dollars-.5)
                messagebox.showinfo(None, "You still have "+ str(money_in_dollars) +" left. ")
            if item == 'pretzels':
                money_in_dollars = int(money_in_dollars-1)
                messagebox.showinfo(None, "You still have "+ str(money_in_dollars) +" left. ")
            if item == 'soda':
                money_in_dollars = int(money_in_dollars-1)
                messagebox.showinfo(None, "You still have "+ str(money_in_dollars) +" left. ")
            if item == 'candy bar':
                money_in_dollars = int(money_in_dollars-1.5)
                messagebox.showinfo(None, "You still have "+ str(money_in_dollars) +" left. ")




        # TODO) Call the vending_machine() function and save the money spent
        #  in a variable, for example:
        #  money_spent = vending_machine(money_in_dollars)

        # TODO) If no money was spent, tell the user how much money they still
        #  have and exit the while loop

        # TODO) Otherwise, subtract the money spent from the amount of money
        #  you still have (money_in_dollars)

    # TODO) If there is exactly 0 money left, create a message that
    #  congratulates the user because they maximized their money.
    if money_in_dollars == 0:
        print('Congradulations. You maximized your money.')
    # TODO) If there is a negative amount of money, tell the user they
    #  overspent!
    if money_in_dollars < 0:
        print('Oh no, you overspent.')