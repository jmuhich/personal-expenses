"""Scripts used to help analyze expenses"""

import csv
import logging

def main():
    importCsv('expense-log.csv')

def importCsv(filePath):
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
                row["Account Description"],
                row["Category Tags"],
                row["Payment Method"],
                row["Merchant Type"])
            entry.print()
            line_count += 1
        print(f'Processed {line_count} entries.')

class ExpenseEntry:
    """Expense Entry Object"""

    def __init__(
        self,
        transactionDate,
        dateProcessed,
        withdrawalAmount,
        depositAmount,
        description,
        accountDescription,
        categoryTags,
        paymentMethod,
        merchantType):

        self._transactionDate = transactionDate
        self._dateProcessed = dateProcessed
        self._withdrawalAmount = withdrawalAmount
        self._depositAmount = depositAmount
        self._description = description
        self._accountDescription = accountDescription
        self._categoryTags = categoryTags
        self._paymentMethod = paymentMethod
        self._merchantType = merchantType

    @property
    def transactionDate(self):
        return self._transactionDate

    @property
    def dateProcessed(self):
        return self._dateProcessed
    
    @property
    def withdrawalAmount(self):
        return self._withdrawalAmount
    
    @property
    def depositAmount(self):
        return self._depositAmount
    
    @property
    def description(self):
        return self._description

    @property
    def accountDescription(self):
        return self._accountDescription

    @property
    def categoryTags(self):
        return self._categoryTags

    @property
    def paymentMethod(self):
        return self._paymentMethod
    
    @property
    def merchantType(self):
        return self._merchantType

    def print(self):
        message = (
            "Transaction Date: " + self.transactionDate + "\n"
            "Description: " + self.description + "\n"
            "Withdrawal Amount: " + self.withdrawalAmount + "\n"
            "Payment Method: " + self.paymentMethod + "\n"
            "Merchant Type: " + self.merchantType + "\n"
            "CategoryTags: " + self.categoryTags + "\n"
            "--------------------------------------------------"
        )
        print(message)

            

if __name__ == "__main__":
    main()