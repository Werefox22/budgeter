from argparse import ArgumentTypeError
from datetime import datetime

# to budget, we need to know two things: income and expenses
class Paycheck():
	def __init__(self, amount, date=datetime.now()) -> None:
		self.amount = amount
		self.date = date

	def __str__(self) -> str:
		return f'${self.amount}'


class Income():
	paychecks = []
	def __init__(self, name, period=-1) -> None:
		self.name = name
		self.period = period

	def add_paycheck(self, paycheck):
		if type(paycheck) is Paycheck:
			self.paychecks.append(paycheck)
			print(type(paycheck))

		elif type(paycheck) is float or type(paycheck) is int:
			self.paychecks.append(Paycheck(paycheck, datetime.now()))
			print(type(paycheck))
			
		else:
			raise ArgumentTypeError("Added paycheck was not of type Paycheck, int, or float")
	
	def print_paychecks(self):
		for p in self.paychecks:
			print(p)
	
	def __str__(self) -> str:
		return f'{self.name}'

check1 = Paycheck(906.29)
check2 = Paycheck(803.23)
check3 = Paycheck(855.76)

income = Income("Jack's Income")

income.add_paycheck(check1)
income.add_paycheck(check2)
income.add_paycheck(check3)
income.add_paycheck(123.45)
income.add_paycheck(900)
# income.add_paycheck("uh oh!") -> Throws ArgumentTypeError

income.print_paychecks()