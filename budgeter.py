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
	def __init__(self, name) -> None:
		self.name = name
		self.paychecks = []

	def add_paycheck(self, new_check):
		if type(new_check) is Paycheck:
			self.paychecks.append(new_check)

		elif type(new_check) is float or type(new_check) is int:
			self.paychecks.append(Paycheck(new_check, datetime.now()))

		else:
			raise ArgumentTypeError(f"Added paycheck {type(new_check)} was not type Paycheck, float, or int")
	
	def add_paychecks(self, new_checks):
		for p in new_checks:
			self.add_paycheck(p)
	
	def print_paychecks(self):
		for p in self.paychecks:
			print(p)
	
	def get_average(self):
		if len(self.paychecks) == 0:
			return 0

		sum = 0
		for i in range(len(self.paychecks)):
			sum += self.paychecks[i]
		return sum / len(self.paychecks)
	
	def __str__(self) -> str:
		return f'{self.name}\n  Average: ${round(self.get_average(), 2)}\n'

check1 = Paycheck(906.29)
check2 = Paycheck(803.23)
check3 = Paycheck(855.76)

income = Income("Jack's Income")

income.add_paychecks([check1, check2, check3, 123.45, 900])

print(income)

income2 = Income("ALDI")
income2.print_paychecks()
print(income2)
income2.add_paycheck(100)
income2.print_paychecks()
print(income2)
print(income)
print(income.paychecks[-1])