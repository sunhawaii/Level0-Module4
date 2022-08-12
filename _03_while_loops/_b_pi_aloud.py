"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    pi_str=str(3.1415926535897932384)
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit

    pi_digit2=1
    pi_digits3=4

    print(pi_str[0], pi_str[1], pi_str[2], pi_str[3])
    # TODO) Use a while loop to keep asking for the next digit of pi
    x=4
    pi_answer = 1
    y = 0
    while pi_answer == 1:

        pi_question = simpledialog.askstring(None, "What is the next digit of pi?")
        if pi_question == pi_str[x]:
            pi_answer = 1
            x = x+1
            y = y+1
            print('you are correct')
        else:
            pi_answer = 2
            print('you are incorrect')
    print('You were able to get '+ str(y) +' amount of pi digit(s) correctly.')
        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
