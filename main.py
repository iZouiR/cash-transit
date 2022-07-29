import tkinter
from tkinter import ttk

import database
import checkers
import messages

from threading import Thread

transaction_amount = 0

# Creation of window
window = tkinter.Tk()
window.title('CashTransit')
window.iconphoto(False, tkinter.PhotoImage(file='icon.png'))
window.geometry('1250x550+335+265')
window.resizable(False, False)

# Creation of canvas
canvas = tkinter.Canvas(window, width=1250, height=550, bg='white')
canvas.pack()

# Drawing bank cards
card_image = tkinter.PhotoImage(file='card.png')
card_image = card_image.subsample(2, 2)
canvas.create_image(30, 20, anchor='nw', image=card_image)
canvas.create_image(695, 20, anchor='nw', image=card_image)

# Creation of input forms for cards numbers
from_a_entry = tkinter.Entry(font=('Allenoire', 27, 'bold'), relief=tkinter.RAISED, bd=3)
from_a_entry.place(x=85, y=200, width=90, height=35)
from_b_entry = tkinter.Entry(font=('Allenoire', 27, 'bold'), relief=tkinter.RAISED, bd=3)
from_b_entry.place(x=195, y=200, width=90, height=35)
from_c_entry = tkinter.Entry(font=('Allenoire', 27, 'bold'), relief=tkinter.RAISED, bd=3)
from_c_entry.place(x=305, y=200, width=90, height=35)
from_d_entry = tkinter.Entry(font=('Allenoire', 27, 'bold'), relief=tkinter.RAISED, bd=3)
from_d_entry.place(x=415, y=200, width=90, height=35)

to_a_entry = tkinter.Entry(font=('Allenoire', 27, 'bold'), relief=tkinter.RAISED, bd=3)
to_a_entry.place(x=750, y=200, width=90, height=35)
to_b_entry = tkinter.Entry(font=('Allenoire', 27, 'bold'), relief=tkinter.RAISED, bd=3)
to_b_entry.place(x=860, y=200, width=90, height=35)
to_c_entry = tkinter.Entry(font=('Allenoire', 27, 'bold'), relief=tkinter.RAISED, bd=3)
to_c_entry.place(x=970, y=200, width=90, height=35)
to_d_entry = tkinter.Entry(font=('Allenoire', 27, 'bold'), relief=tkinter.RAISED, bd=3)
to_d_entry.place(x=1080, y=200, width=90, height=35)

# Creation of input forms for cards cvv codes
from_cvv_entry = tkinter.Entry(font=('Allenoire', 18, 'bold'), relief=tkinter.RAISED, bd=3, show='*',
                               justify=tkinter.CENTER)
from_cvv_entry.place(x=90, y=245, width=40, height=20)

to_cvv_entry = tkinter.Entry(font=('Allenoire', 18, 'bold'), relief=tkinter.RAISED, bd=3, show='*',
                             justify=tkinter.CENTER)
to_cvv_entry.place(x=755, y=245, width=40, height=20)

# Creation of input forms for cards date
from_month_entry = tkinter.Entry(font=('Allenoire', 15, 'bold'), relief=tkinter.RAISED, bd=3)
from_month_entry.place(x=260, y=257, width=30, height=25)
from_year_entry = tkinter.Entry(font=('Allenoire', 15, 'bold'), relief=tkinter.RAISED, bd=3)
from_year_entry.place(x=307, y=257, width=30, height=25)

to_month_entry = tkinter.Entry(font=('Allenoire', 15, 'bold'), relief=tkinter.RAISED, bd=3)
to_month_entry.place(x=925, y=257, width=30, height=25)
to_year_entry = tkinter.Entry(font=('Allenoire', 15, 'bold'), relief=tkinter.RAISED, bd=3)
to_year_entry.place(x=972, y=257, width=30, height=25)

# Creation of input forms for cards owners
from_owner_entry = tkinter.Entry(font=('Allenoire', 15, 'bold'), relief=tkinter.RAISED, bd=3)
from_owner_entry.place(x=90, y=290, width=228, height=28)

to_owner_entry = tkinter.Entry(font=('Allenoire', 15, 'bold'), relief=tkinter.RAISED, bd=3)
to_owner_entry.place(x=755, y=290, width=228, height=28)

# Creation of transaction amount label
transaction_amount_label = tkinter.Label(text=f'{transaction_amount} $', font=('Allenoire', 15, 'bold'),
                                         relief=tkinter.RAISED, bd=3, justify=tkinter.CENTER)
transaction_amount_label.place(x=555, y=340, width=140, height=25)

# Creation of checker-thread for input forms
checker_thread = Thread(target=checkers.all_cycle, args=(from_a_entry, from_b_entry, from_c_entry, from_d_entry,
                                                         to_a_entry, to_b_entry, to_c_entry, to_d_entry,
                                                         from_cvv_entry, to_cvv_entry, from_month_entry,
                                                         from_year_entry, to_month_entry, to_year_entry,
                                                         from_owner_entry, to_owner_entry))
checker_thread.start()

# Creation of info-button
info_button = tkinter.Button(text='?', font=('Allenoire', 50, 'bold'), command=messages.info)
info_button.place(x=590, y=15, width=70, height=70)


def from_card():
    from_number = from_a_entry.get() + from_b_entry.get() + from_c_entry.get() + from_d_entry.get()
    from_cvv = from_cvv_entry.get()
    from_date = from_month_entry.get() + '/' + from_year_entry.get()
    from_owner = from_owner_entry.get()
    card = (from_number, from_cvv, from_date, from_owner)
    return card


def to_card():
    to_number = to_a_entry.get() + to_b_entry.get() + to_c_entry.get() + to_d_entry.get()
    to_cvv = to_cvv_entry.get()
    to_date = to_month_entry.get() + '/' + to_year_entry.get()
    to_owner = to_owner_entry.get()
    card = (to_number, to_cvv, to_date, to_owner)
    return card


def transit():
    database.transit(from_card(), to_card(), transaction_amount)


# Creation of transit-button
transit_button = tkinter.Button(text='->', font=('Allenoire', 30, 'bold'), command=transit)
transit_button.place(x=590, y=100, width=70, height=140)


def swap():
    from_card_credits = (from_a_entry.get(), from_b_entry.get(), from_c_entry.get(), from_d_entry.get(),
                         from_cvv_entry.get(), from_month_entry.get(), from_year_entry.get(), from_owner_entry.get())
    to_card_credits = (to_a_entry.get(), to_b_entry.get(), to_c_entry.get(), to_d_entry.get(), to_cvv_entry.get(),
                       to_month_entry.get(), to_year_entry.get(), to_owner_entry.get())

    from_a_entry.delete(0, "end")
    from_b_entry.delete(0, "end")
    from_c_entry.delete(0, "end")
    from_d_entry.delete(0, "end")
    from_cvv_entry.delete(0, "end")
    from_month_entry.delete(0, "end")
    from_year_entry.delete(0, "end")
    from_owner_entry.delete(0, "end")

    to_a_entry.delete(0, "end")
    to_b_entry.delete(0, "end")
    to_c_entry.delete(0, "end")
    to_d_entry.delete(0, "end")
    to_cvv_entry.delete(0, "end")
    to_month_entry.delete(0, "end")
    to_year_entry.delete(0, "end")
    to_owner_entry.delete(0, "end")

    from_a_entry.insert(0, to_card_credits[0])
    from_b_entry.insert(0, to_card_credits[1])
    from_c_entry.insert(0, to_card_credits[2])
    from_d_entry.insert(0, to_card_credits[3])
    from_cvv_entry.insert(0, to_card_credits[4])
    from_month_entry.insert(0, to_card_credits[5])
    from_year_entry.insert(0, to_card_credits[6])
    from_owner_entry.insert(0, to_card_credits[7])

    to_a_entry.insert(0, from_card_credits[0])
    to_b_entry.insert(0, from_card_credits[1])
    to_c_entry.insert(0, from_card_credits[2])
    to_d_entry.insert(0, from_card_credits[3])
    to_cvv_entry.insert(0, from_card_credits[4])
    to_month_entry.insert(0, from_card_credits[5])
    to_year_entry.insert(0, from_card_credits[6])
    to_owner_entry.insert(0, from_card_credits[7])


# Creation of swap-button
swap_button = tkinter.Button(text='⇆', font=('Allenoire', 50, 'bold'), command=swap)
swap_button.place(x=590, y=255, width=70, height=70)


def increase_transaction_amount():
    global transaction_amount
    transaction_amount += 10
    transaction_amount_label['text'] = f'{transaction_amount} $'


def decrease_transaction_amount():
    global transaction_amount
    transaction_amount -= 10
    if transaction_amount < 0:
        transaction_amount = 0
    transaction_amount_label['text'] = f'{transaction_amount} $'


# Creation of transaction amount increase-button
transaction_amount_increase_button = tkinter.Button(text='+', font=('Allenoire', 40, 'bold'),
                                                    command=increase_transaction_amount)
transaction_amount_increase_button.place(x=590, y=380, width=70, height=70)

# Creation of transaction amount decrease-button
transaction_amount_decrease_button = tkinter.Button(text='-', font=('Allenoire', 40, 'bold'),
                                                    command=decrease_transaction_amount)
transaction_amount_decrease_button.place(x=590, y=465, width=70, height=70)


def increase_from_cash():
    global transaction_amount
    database.gift(from_card(), transaction_amount)


def increase_to_cash():
    global transaction_amount
    database.gift(to_card(), transaction_amount)


# Creation of from bank card cash increase-button
from_cash_increase_button = tkinter.Button(text='$$$', font=('Allenoire', 30, 'bold'), command=increase_from_cash)
from_cash_increase_button.place(x=100, y=390, width=70, height=70)

# Creation of to bank card cash increase-button
to_cash_increase_button = tkinter.Button(text='$$$', font=('Allenoire', 30, 'bold'), command=increase_to_cash)
to_cash_increase_button.place(x=1080, y=390, width=70, height=70)


def cards():
    all_cards_window = tkinter.Tk()
    all_cards_window.title('cards from database')
    all_cards_window.resizable(False, False)

    all_cards_frame = tkinter.Frame(all_cards_window)
    all_cards_frame.pack()

    card_columns = ["ID", "Card Number", "CVV", "Card Date", "Card Owner", "Card Cash"]

    all_cards_tablet = ttk.Treeview(all_cards_frame, show='headings')
    all_cards_tablet['columns'] = card_columns

    for column in card_columns:
        all_cards_tablet.heading(column, text=column, anchor='center')
        all_cards_tablet.column(column, anchor='center')

    all_cards = database.cards()
    for card in all_cards:
        all_cards_tablet.insert('', tkinter.END, values=card)

    all_cards_tablet_scroller = ttk.Scrollbar(all_cards_frame, command=all_cards_tablet.yview)
    all_cards_tablet_scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    all_cards_tablet.configure(yscrollcommand=all_cards_tablet_scroller.set)
    all_cards_tablet.pack(expand=tkinter.YES, fill=tkinter.BOTH)

    all_cards_window.mainloop()


# Creation of cards-button
cards_button = tkinter.Button(text='base', font=('Allenoire', 30, 'bold'), command=cards)
cards_button.place(x=220, y=390, width=210, height=70)


def story():
    transactions_window = tkinter.Tk()
    transactions_window.title('transactions from database')
    transactions_window.resizable(False, False)

    transactions_frame = tkinter.Frame(transactions_window)
    transactions_frame.pack()

    transaction_columns = ["ID", "Sender", "Receiver", "Amount", "Date"]

    transactions_tablet = ttk.Treeview(transactions_frame, show='headings')
    transactions_tablet['columns'] = transaction_columns

    for column in transaction_columns:
        transactions_tablet.heading(column, text=column, anchor='center')
        transactions_tablet.column(column, anchor='center')

    transactions = database.story()
    for transaction in transactions:
        transactions_tablet.insert('', tkinter.END, values=transaction)

    transactions_tablet_scroller = ttk.Scrollbar(transactions_frame, command=transactions_tablet.yview)
    transactions_tablet_scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    transactions_tablet.configure(yscrollcommand=transactions_tablet_scroller.set)
    transactions_tablet.pack(expand=tkinter.YES, fill=tkinter.BOTH)

    transactions_window.mainloop()


# Creation of story-button
story_button = tkinter.Button(text='story', font=('Allenoire', 30, 'bold'), command=story)
story_button.place(x=820, y=390, width=210, height=70)

window.mainloop()
