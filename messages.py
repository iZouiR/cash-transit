import tkinter.messagebox


def info():
    message = 'An application for simulation of cashless transfer from card to card.' \
              ' Fill in the input forms, specify the amount of cash and click "->"\n' \
              '\n- Click the "$" button on the left or on the right' \
              ' to get money as a gift\n' \
              '\n- Click the "swap" button in order' \
              ' to swap the cards data\n' \
              '\n- Click the "cards" button to display' \
              ' the list of cards registered in the database\n' \
              '\n- Click the "story" button to display recently performed operations'
    tkinter.messagebox.showinfo('Info', message)


def transaction_success():
    message = 'Transaction was successful'
    tkinter.messagebox.showinfo('Success', message)


def transaction_error():
    message = 'Transaction failed'
    tkinter.messagebox.showerror('Failure', message)
