class fd:	
	Amount=0
	Interest=0
	Division=1
	simple_intrest=0
	values=[]
	Time=0
	period=1
	
	def fill(self,Amount,Interest,Time,Choice,period):
		self.Amount=Amount
		self.values.append(Amount)
		self.Interest=Interest
		self.Time=Time
		self.period=period
		self.Choice=Choice

	def clacu(self):
		if self.Choice == 1:
			pass
		elif self.Choice == 2:
			self.Interest = self.Interest/2
			self.Division = 2
		elif self.Choice == 3:
			self.Interest = self.Interest/4
			self.Division = 4
		elif self.Choice == 4:
			self.Interest = self.Interest/12
			self.Division = 12
		if self.Time == 2:
			for b in range(0,self.period):
				for l in range(0,self.Division):
					i = self.Interest/100
					i=i+1
					self.Amount = i * self.Amount
					self.values.append(self.Amount)
			return self.values
		elif self.Time == 1:
			t = (self.Amount * self.Interest)/100
			for b in range(0,self.period):
				for i in range(0,self.Division):
					self.simple_intrest = self.simple_intrest + t
					temp = self.simple_intrest + self.Amount
					self.values.append(temp)
			return self.values
	def refill(self):
		self.Amount=0
		self.Interest=0
		self.Division=1
		self.simple_intrest=0
		del self.values[:]
		self.Time=0
		self.period=1
			


# Amount=eval(input("enter the Principal Amount"))
# Interest=eval(input("enter the rate of interest"))
# print("1 : simple\n2 : compound")
# Time=eval(input("Enter your choice"))
# print("1 : Annually\n2 : Half yearly\n3 : Quarterly\n 4 : Monthly") 
# Choice=eval(input('Enter your choice'))
# period=int(input("enter the period"))

# f=fd(Amount,Interest,Time,Choice,period)
# print(f.clacu())


