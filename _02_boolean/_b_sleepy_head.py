"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle

if __name__ == '__main__':


    weekend = True
    weekday = False


    if weekend:
        print('Today is a weekend!')
        if weekday:
            print('Today is a weekday!')
        else:
            print('Today is not a weekday.' )


    exam_failure = True
    exam_sucess = False


    if exam_failure:
        print('You are a failure and failed the exam.')
        if exam_sucess:
            print('You succeded in passing this exam.')




    game_over = True
    game_going = False

    if game_over:
        print('The game is over.')



    turt=turtle.Turtle

    shape_red = True
    shape_square = True

    if shape_red:
        turt.fillcolor('red')
        turt.beginfill()
        if shape_square:
            for i in range(4):
                turt.forward(100)
                turt.right(90)
    if shape_red and shape_square:
        turt.fillcolor('red')
        turt.beginfill()
        turt.forward(100)
        turt.right(90)

    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    pass
