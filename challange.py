# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter


mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('300x400-8-200')
mainWindow['padx'] = 12

mainWindow.columnconfigure(0, weight=1)

mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=1)


result = tkinter.Entry(mainWindow) # method for text field
result.grid(row=0, column=0, sticky='nsew', pady=10, ipady=8)

# Adding buttons
buttonsFrame = tkinter.Frame(mainWindow)
buttonsFrame.grid(row=1, column=0, sticky='nsew')


calculateRows = [
    ['C','CE'],
    ['7', '8', '9','+'],
    ['4','5','6','-'],
    ['1','2','3','*'],
    ['0','=', '/']
]

for row_index, row in enumerate(calculateRows):
    col_index = 0
    item_index = 0

    while item_index < len(row):
        value = row[item_index]

        if value == "=":
            buttonsFrame.columnconfigure(col_index, weight=1)
            buttonsFrame.columnconfigure(col_index + 1, weight=1)
            button = tkinter.Button(buttonsFrame, pady=10, text=value)

            button.grid(row=row_index, column=col_index, sticky='nsew', columnspan=2)

            col_index += 2
            item_index += 1

        else:
            buttonsFrame.columnconfigure(col_index, weight=1)
            button = tkinter.Button(buttonsFrame, pady=10, text=value)

            button.grid(row=row_index, column=col_index, sticky='nsew')

            col_index += 1
            item_index += 1

mainWindow.resizable(width=True, height=False)
mainWindow.mainloop()