import sqlite3
from datetime import datetime

import messages

db = sqlite3.connect('cash_transit.db')


def exists(card):
    cursor = db.cursor()
    cursor.execute("""SELECT id FROM cards
    WHERE card_number = (?) AND card_cvv = (?) AND card_date = (?) AND card_owner = (?)""", card)
    return cursor.fetchone() is not None


def add(card):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO cards (card_number, card_cvv, card_date, card_owner)
    VALUES (?, ?, ?, ?)""", card)
    db.commit()


def cash(card):
    cursor = db.cursor()
    cursor.execute("""SELECT card_cash FROM cards
    WHERE card_number = (?) AND card_cvv = (?) AND card_date = (?) AND card_owner = (?)""", card)
    return cursor.fetchone()[0]


def transit(from_card, to_card, transaction_amount):
    if exists(from_card) and exists(to_card) and transaction_amount > 0:
        cursor = db.cursor()
        if transaction_amount <= cash(from_card):
            cursor.execute("""UPDATE cards SET card_cash = (card_cash - (?))
                            WHERE card_number = (?)""", (transaction_amount, from_card[0]))
            cursor.execute("""UPDATE cards SET card_cash = (card_cash + (?))
                            WHERE card_number = (?)""", (transaction_amount, to_card[0]))
            cursor.execute("""INSERT INTO transactions
            (from_number, to_number, transaction_amount, transaction_date)
            VALUES (?, ?, ?, ?)""", (from_card[0], to_card[0], transaction_amount, datetime.now()))
            db.commit()
            messages.transaction_success()
        else:
            messages.transaction_error()
    else:
        messages.transaction_error()


def gift(to_card, transaction_amount):
    if exists(to_card):
        cursor = db.cursor()
        cursor.execute("""UPDATE cards SET card_cash = (card_cash + (?))
        WHERE card_number = (?)""", (transaction_amount, to_card[0]))
        db.commit()


def cards():
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM cards""")
    return cursor.fetchall()


def story():
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM transactions""")
    return cursor.fetchall()
