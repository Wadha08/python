import datetime
class Employee:

	def __init__(self,name,age,salary,employment_date):
		self.name = name
		self.age= age
		self.salary = salary
		self.employment_date = employment_date

	def get_working_years(self):
		working_years = int(datetime.date.today().year)-int(self.employment_date)
		return working_years

	def __str__(self):
		return "Employee \nname: {} ,age: {}, Salary: {} , working hours: {}".format(self.name,self.age,self.salary,self.get_working_years())

class Manager(Employee):

	def __init__(self,name,age,salary,employment_date,bonus_percentage):
		super().__init__(name,age,salary,employment_date)
		self.bonus_percentage=bonus_percentage

	def get_bonus(self):
		return float(self.bonus_percentage)*float(self.salary)

	def __str__(self):
		return "Managers \nname: {} ,age: {}, Salary: {} , working hours: {} , Bonus: {}".format(self.name,self.age,self.salary,self.get_working_years(),self.get_bonus())


print("Welcome to HR Pro 2019")
print("choose an action to do:")
print("1. show employees")
print("2. show managers")
print("3. add an employee")
print("4. add a manager")
print("5. exit")

option = int(input("what would you like to do?: "))
print("-----------------")
#list of objects
Employees=[]
Managers =[]

while option != 5:

	if option == 1:
		for i in Employees:
		 	print(i)

	elif option == 2:
   		for i in Managers:
   			print(i)
	
	elif option == 3:
		name = input("Name: ")
		age = input("age: ")
		salary = input("salary: ")
		employement_year = input("employement year: ")
		e1 = Employee(name,age,salary,employement_year)
		Employees.append(e1)
		print("Employee added succesfully")

	elif option ==4:
		name = input("Name: ")
		age = input("age: ")
		salary = input("salary: ")
		employement_year = input("employement year: ")
		bonusPrecentage = input("bonus percentage: ")
		m1 = Manager(name,age,salary,employement_year,bonusPrecentage)
		Managers.append(m1)
		print("Employee added succesfully")
	else:
		print("invalid option")

	option = int(input("what would you like to do?: "))
	print("-----------------")












