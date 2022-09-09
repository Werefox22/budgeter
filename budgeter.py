from datetime import datetime

# to budget, we need to know two things: income and expenses
class Paycheck():
	def __init__(self, amount, date) -> None:
		self.amount = amount
		self.date = date

	def __str__(self) -> str:
		return f'${self.amount}'
	


class Income():
	paychecks = []
	def __init__(self, name) -> None:
		self.name = name

check = Paycheck(906.29, datetime.now())
print(check)