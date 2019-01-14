import logging
from datetime import datetime
from decimal import Decimal

class ExpenseEntry:
    """Expense Entry Object"""

    def __init__(
        self,
        transactionDate,
        dateProcessed,
        withdrawalAmount,
        depositAmount,
        description,
        category,
        paymentMethod,
        account,
        merchantType,
        accountDescription):

        if transactionDate:
            self._transactionDate = datetime.strptime(transactionDate, '%m/%d/%y')
        else:
            self._transactionDate = None

        if dateProcessed:
            self._dateProcessed = datetime.strptime(dateProcessed, '%m/%d/%y') 
        else:
            self._dateProcessed = None
        
        if withdrawalAmount:
            self._withdrawalAmount = Decimal(withdrawalAmount.strip('$').replace(',', ''))
        else:
            self._withdrawalAmount = None

        if depositAmount:
            self._depositAmount = Decimal(depositAmount.strip('$').replace(',', ''))
        else:
            self._depositAmount = None

        self._description = description
        self._category = category
        self._paymentMethod = paymentMethod
        self._account = account
        self._merchantType = merchantType
        self._accountDescription = accountDescription

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
    def withdrawalAmountAsString(self):
        return str(self._withdrawalAmount)

    @property
    def withdrawalAmountForDb(self):
        if self._withdrawalAmount:
            return str(self._withdrawalAmount)
        else:
            return None
    
    @property
    def depositAmount(self):
        return self._depositAmount

    @property
    def depositAmountAsString(self):
        return str(self._depositAmount)

    @property
    def depositAmountForDb(self):
        if self._depositAmount:
            return str(self._depositAmount)
        else:
            return None
    
    @property
    def description(self):
        return self._description

    @property
    def category(self):
        return self._category

    @property
    def paymentMethod(self):
        return self._paymentMethod

    @property
    def account(self):
        return self._account
    
    @property
    def merchantType(self):
        return self._merchantType

    @property
    def accountDescription(self):
        return self._accountDescription

    def print(self):
        message = (
            "Transaction Date: " + self.transactionDate.strftime('%m/%d/%y') + "\n"
            "Description: " + self.description + "\n"
            "Withdrawal Amount: $" + self.withdrawalAmountAsString + "\n"
            "Payment Method: " + self.paymentMethod + "\n"
            "Account: " + self.account + "\n"
            "Merchant Type: " + self.merchantType + "\n"
            "Category: " + self.category + "\n"
            "--------------------------------------------------"
        )
        print(message)

    def importToDb(self, dbCursor):
        dbCursor.execute('''
            INSERT INTO expenses(
                transactionDate,
                dateProcessed,
                withdrawalAmount,
                depositAmount,
                description,
                category,
                paymentMethod,
                account,
                merchantType,
                accountDescription)
            VALUES(?,?,?,?,?,?,?,?,?,?)
        ''', (
            self.transactionDate,
            self.dateProcessed,
            self.withdrawalAmountForDb,
            self.depositAmountForDb,
            self.description,
            self.category,
            self.paymentMethod,
            self.account,
            self.merchantType,
            self.accountDescription))