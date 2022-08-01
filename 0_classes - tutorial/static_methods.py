class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

        Employee.num_of_emps += 1
    
    def fullname(self): 
        return self.first + ' ' + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod        # receives CLASS as the first argument instead of the instance (object)
    def set_raise_amt(cls, amount):         # instead of 'self', use 'cls'
        cls.raise_amt = amount
    
    @classmethod        # class methods used as alternate constructures -> creating new objects 
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)      # creates new employee(object)

    @staticmethod       # use static when you dont access instance or class anywhere in method
    def is_workday(day):    # staticmethods don't take instance or class as first argument
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Leena', 'Kang', 50)
emp_2 = Employee('Wanda', 'Vision', 60)





