""" UI Calculator with buttons """
from tkinter import (
    Tk,
    Label,
    Button
)

str_display_calc = ""
label = None
nb2 = None
operator = None


def add_character(nb):
    """
        add character on calculator screen
        :param nb: a string is expected
    """
    global str_display_calc
    global label
    # example '1' + '3' = '13'
    str_display_calc = str_display_calc + nb
    # update UI label
    label["text"] = str_display_calc


def reset():
    """
        function when 'C' button is pressed
        we reset the screen
    """
    global str_display_calc
    global label
    global nb2
    str_display_calc = ""
    nb2 = ""  # ???
    label["text"] = ""


def add():
    """
        function when '+' button is pressed
        we want to add numbers
    """
    global str_display_calc
    global nb2
    global operator
    nb2 = float(str_display_calc)
    str_display_calc = ""
    operator = 1


def subtract():
    """
        function when '-' button is pressed
        we want to subtract numbers
    """
    global str_display_calc
    global nb2
    global operator
    nb2 = float(str_display_calc)
    str_display_calc = ""
    operator = 2


def multi():
    """
        function when '*' button is pressed
        we want to multiply numbers
    """
    global str_display_calc
    global label
    global operator
    global nb2
    nb2 = float(str_display_calc)
    str_display_calc = ""
    operator = 3


def div():
    """
        function when '/' button is pressed
        we want to divide numbers
    """
    global str_display_calc
    global nb2
    global operator
    nb2 = float(str_display_calc)
    str_display_calc = ""
    operator = 4


def equal():
    """
        function when '=' button is pressed
        we want to compute result
    """
    global str_display_calc
    global label
    global operator
    global nb2
    str_display_calc = float(str_display_calc)  # Cast in float
    if operator == 1:
        result = round(nb2 + str_display_calc, 10)  # round with 2 digits
    if operator == 2:
        result = round(nb2 - str_display_calc, 10)
    if operator == 3:
        result = round(nb2 * str_display_calc, 10)
    if operator == 4:
        result = round(nb2 / str_display_calc, 10)
    label["text"] = result
    str_display_calc = str(result)  # Cast in string
    result = 0


def main():
    """ main function whose purpose is to launch UI """
    global label
    # init window
    window = Tk()
    window.title("Calculator v1")

    # define our main label emulating calculator screen
    label = Label(window, text="0")
    label.place(x=10, y=10)

    # define all buttons on our calculator
    # argument command expects a function
    # we create some lambda functions using add_character
    # with a specific argument
    # Since we do not modify after creation, we do not need
    # to store the result into variable
    Button(
        window,
        text=" 1 ",
        command=lambda: add_character("1")
    ).place(x=10, y=50)
    Button(
        window,
        text=" 2 ",
        command=lambda: add_character("2")
    ).place(x=30, y=50)
    Button(
        window,
        text=" 3 ",
        command=lambda: add_character("3")
    ).place(x=50, y=50)
    Button(
        window,
        text=" 4 ",
        command=lambda: add_character("4")
    ).place(x=10, y=70)
    Button(
        window,
        text=" 5 ",
        command=lambda: add_character("5")
    ).place(x=30, y=70)
    Button(
        window,
        text=" 6 ",
        command=lambda: add_character("6")
    ).place(x=50, y=70)
    Button(
        window,
        text=" 7 ",
        command=lambda: add_character("7")
    ).place(x=10, y=90)
    Button(
        window,
        text=" 8 ",
        command=lambda: add_character("8")
    ).place(x=30, y=90)
    Button(
        window,
        text=" 9 ",
        command=lambda: add_character("9")
    ).place(x=50, y=90)
    Button(
        window,
        text=" 0 ",
        command=lambda: add_character("0")
    ).place(x=10, y=110)
    Button(
        window,
        text=" . ",
        command=lambda: add_character(".")
    ).place(x=30, y=110)
    Button(
        window,
        text=" C ",
        command=reset
    ).place(x=50, y=110)
    Button(
        window,
        text=" + ",
        command=add
    ).place(x=90, y=50)
    Button(
        window,
        text=" - ",
        command=subtract
    ).place(x=110, y=50)
    Button(
        window,
        text=" * ",
        command=multi
    ).place(x=130, y=50)
    Button(
        window,
        text=" / ",
        command=div
    ).place(x=150, y=50)
    Button(
        window,
        text=" = ",
        command=equal
    ).place(x=30, y=150)
    window.mainloop()


if __name__ == '__main__':
    # we launch UI only if this script is the main one
    main()
