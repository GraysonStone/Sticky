class ToDo():
	entry=""
	day=0
	month=0
	year=0
	date=0

	def __init__(self,entry,date):
		self.entry=entry[0:len(entry)-1]
		hold=date
		self.date=date[0:len(date)-1]
		self.month=hold[0:hold.index('/')]
		hold=hold[hold.index('/')+1:hold.index('\n')]
		self.day=hold[0:hold.index('/')]
		self.year=hold[hold.index('/')+1:len(hold)]
		

		


