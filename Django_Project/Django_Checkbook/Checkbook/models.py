from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=60, default="")
    lastName = models.CharField(max_length=60, default="")
    startingBal = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)

    Accounts = models.Manager()

    def __str__(self):
        return "{}, {}".format(self.lastName.title(), self.firstName.title())


TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()

