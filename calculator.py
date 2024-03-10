import tkinter as tk

# Function to update the display when a button is clicked
def button_click(symbol):
    current = display_var.get()
    if symbol == 'C':
        display_var.set('')
    elif symbol == '=':
        try:
            result = eval(current)
            display_var.set(str(result))
        except:
            display_var.set('Error')
    else:
        display_var.set(current + symbol)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Variable to store display value
display_var = tk.StringVar()

# Entry widget to display result
display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), bd=10, justify='right')
display.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Define button symbols
button_symbols = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for symbol, row, col in button_symbols:
    button = tk.Button(root, text=symbol, font=('Arial', 16), padx=20, pady=10,
                        command=lambda s=symbol: button_click(s))
    button.grid(row=row, column=col, sticky='nsew')

# Configure grid rows and columns
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
