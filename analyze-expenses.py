"""Scripts used to help analyze expenses"""

import csv
import logging
import sqlite3
from expense_entry import ExpenseEntry

def main():
    db = sqlite3.connect('test.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY,
            transactionDate TEXT,
            dateProcessed TEXT,
            withdrawalAmount DECIMAL(19, 2),
            depositAmount DECIMAL(19, 2),
            description TEXT,
            category TEXT,
            paymentMethod TEXT,
            account TEXT,
            merchantType TEXT,
            accountDescription TEXT)
    ''')
    importCsv('../expense-log-2019-01-09.csv', cursor)
    db.commit()
    db.close()

def importCsv(filePath, dbCursor):
    with open(filePath, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = None
        for row in csv_reader:
            if line_count is None:
                line_count = 0
            entry = ExpenseEntry(
                row["Transaction Date"],
                row["Date Processed"],
                row["Withdrawal Amount"],
                row["Deposit Amount"],
                row["Description"],
                row["Category"],
                row["Payment Method"],
                row["Account"],
                row["Merchant Type"],
                row["Account Description"])
            entry.print()
            entry.importToDb(dbCursor)
            line_count += 1
        print(f'Processed {line_count} entries.')         

if __name__ == "__main__":
    main()