
class Person(object):
	
	
	def __init__(self, name):
		self.name = name


	def getName(self):
		return self.name

	
	def isEmployee(self):
		return False



class Employee(Person):


	def isEmployee(self):
		return True

emp = Person("Lavanya") 
print(emp.getName(), emp.isEmployee())

emp = Employee("mani") 
print(emp.getName(), emp.isEmployee())
