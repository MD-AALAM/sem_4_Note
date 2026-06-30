class Employee:
    company="Apple"
    def show(self):
        print(f"the name is{self.name} and the company is{self.company}")
    
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company

e1=Employee()
e1.name="John"
e1.show()
e1.change_company("Microsoft")
e1.show()
print(Employee.company)
