from argparse import ArgumentTypeError
from datetime import datetime

# to budget, we need to know two things: income and expenses
class Paycheck():
	def __init__(self, amount, date=datetime.now()) -> None:
		self.amount = amount
		self.date = date

	def __str__(self) -> str:
		return f'${self.amount}'
	
	def __add__(self, other):
		return self.amount + other
	
	def __radd__(self, other):
		return self.__add__(other)
	
	def __sub__(self, other):
		return self.amount - other
	
	def __rsub__(self, other):
		return self.__sub__(other)
	


class Income():
	paychecks = []
	def __init__(self, name, period=-1) -> None:
		self.name = name
		self.period = period

	def add_paycheck(self, paycheck):
		if type(paycheck) is Paycheck:
			self.paychecks.append(paycheck)

		elif type(paycheck) is float or type(paycheck) is int:
			self.paychecks.append(Paycheck(paycheck, datetime.now()))

		else:
			raise ArgumentTypeError(f"Added paycheck {type(paycheck)} was not type Paycheck, float, or int")
	
	def add_paychecks(self, paychecks):
		for p in paychecks:
			self.add_paycheck(p)
	
	def print_paychecks(self):
		for p in self.paychecks:
			print(p)
	
	def get_average(self):
		sum = 0
		for i in range(len(self.paychecks)):
			sum += self.paychecks[i]
		return sum / len(self.paychecks)
	
	def __str__(self) -> str:
		return f'{self.name}'

check1 = Paycheck(906.29)
check2 = Paycheck(803.23)
check3 = Paycheck(855.76)

income = Income("Jack's Income")

income.add_paychecks([check1, check2, check3, 123.45, 900])

print(income.get_average())