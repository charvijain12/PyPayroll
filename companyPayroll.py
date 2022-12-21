# In practice, classes sure have more logic.
from abc import ABC, abstractmethod

class StaffMember:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f'{self.__class__.__name__} - Name: {self.name} - Address: {self.address}'

    def __lt__(self, other):
        if type(self) is not type(other):
            return self.__class__.__name__ < other.__class__.__name__

        return (self.name, self.address) < (other.name, other.address)

class Employee(StaffMember):
    def __init__(self, name, address, day_to_pay):
        super().__init__(name, address)
        self.day_to_pay = day_to_pay


class HourlyEmployee(Employee):
    def __init__(self, name, address, day_to_pay, total_working_hours, salary_per_hour):
        super().__init__(name, address, day_to_pay)
        self.total_working_hours = total_working_hours
        self.salary_per_hour = salary_per_hour

    @property
    def amount_to_pay(self):
        return self.total_working_hours * self.salary_per_hour


class SalariedEmployee(Employee):
    def __init__(self, name, address, day_to_pay, monthly_salary):
        super().__init__(name, address, day_to_pay)
        self.monthly_salary = monthly_salary

    @property
    def amount_to_pay(self):
        return self.monthly_salary


class CommissionSalariedEmployee(SalariedEmployee):
    def __init__(self, name, address, day_to_pay, monthly_salary, commission_rate, current_month_sales):
        super().__init__(name, address, day_to_pay, monthly_salary)
        self.commission_rate = commission_rate
        self.current_month_sales = current_month_sales

    @property
    def amount_to_pay(self):
        return super().amount_to_pay + self.current_month_sales * self.commission_rate


class Volunteer(StaffMember):
    def __init__(self, name, address, current_payment):
        super().__init__(name, address)
        self.current_payment = current_payment

    @property
    def amount_to_pay(self):
        return self.current_payment


class Item:
    def __init__(self, desc, price_per_one, quantity):
        self.desc = desc
        self.price_per_one = price_per_one 
        self.quantity = quantity

    @property
    def price(self):
        return self.price_per_one * self.quantity
    

class Book(Item):
    def __init__(self, desc, price_per_one, quantity, author):
        super().__init__(desc, price_per_one, quantity)
        self.desc = desc
        self.price_per_one = price_per_one 
        self.quantity = quantity
        self.author = author
        
class Food(Item):
    def __init__(self, desc, price_per_one, quantity, expiration_date):
        super().__init__(desc, price_per_one, quantity)
        self.desc = desc
        self.price_per_one = price_per_one 
        self.quantity = quantity
        self.author = expiration_date








class VaidationRule(ABC):
    @abstractmethod
    def is_valid_rule(self, invoice):
        pass

class TaxesVaidationRule(VaidationRule):
    def is_valid_rule(self, invoice):
        print('Validating TaxesVaidationRule')
        return True

class SuppliersDealsVaidationRule(VaidationRule):
    def is_valid_rule(self, invoice):
        print('Validating SuppliersDealsVaidationRule')
        return False


class InvoiceValidator:
    def __init__(self, rules):
        self.rules = rules

    def validate(self, invoice: VaidationRule):
        if not self.rules:
            raise ValueError('Zero rules list.')

        for rule in self.rules:
            if not rule.is_valid_rule(invoice):
                return False
        return True


class MandatoryInvoiceValidator(InvoiceValidator):
    @staticmethod
    def get_instance():
        rules = [TaxesVaidationRule()]
        return MandatoryInvoiceValidator(rules)


class CompleteInvoiceValidator(InvoiceValidator):
    @staticmethod
    def get_instance():
        rules = [TaxesVaidationRule(), SuppliersDealsVaidationRule()]
        return MandatoryInvoiceValidator(rules)


class ValidationError(BaseException):
    pass

class Invoice:
    def __init__(self, invoice_id, validator: InvoiceValidator):
        self.invoice_id = invoice_id
        self.validator = validator
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    @property
    def amount_to_pay(self):
        if not self.validator.validate(self):
            raise ValidationError('One of the invoices are invalid')
        return sum([item.price for item in self.items])

    def __repr__(self):
        return f'{self.__class__.__name__} - Invoice ID {self.invoice_id} - with total # of items {len(self.items)}'

    def __lt__(self, other):
        if type(self) is not type(other):
            return self.__class__.__name__ < other.__class__.__name__

        return (self.invoice_id, len(self.items)) < (other.invoice_id, len(other.items))

class Payroll:
    def __init__(self):
        self.payables = []

    def add_payable(self, payable):
        self.payables.append(payable)

    @property
    def amount_to_pay(self):
        return sum([payable.amount_to_pay for payable in self.payables])

    def __repr__(self):
        self.payables.sort()
        return '\n'.join([repr(payable) for payable in self.payables])


class Company:
    def __init__(self):
        self.payroll = Payroll()

    def fill_data(self, is_mandatory_validator = True):
        self.payroll.add_payable(Volunteer('Most', 'AddressV', 700))
        self.payroll.add_payable(HourlyEmployee('Belal', 'AddressH', 1, 10, 3))
        self.payroll.add_payable(SalariedEmployee('Ziad', 'AddressS1', 2, 3000))
        self.payroll.add_payable(SalariedEmployee('Ashraf', 'AddressS1', 2, 3000))
        self.payroll.add_payable(CommissionSalariedEmployee('Safa', 'AddressC1', 6, 2500, 0.001, 5000))
        self.payroll.add_payable(CommissionSalariedEmployee('ahmed', 'AddressC2', 6, 2500, 0.001, 5000))

        if is_mandatory_validator:
            validator = MandatoryInvoiceValidator.get_instance()
        else:
            validator = CompleteInvoiceValidator.get_instance()
        invoice = Invoice(1234, validator)
        invoice.add_item(Book('book1', 10, 7, ''))
        invoice.add_item(Food('food1', 5, 6, ''))
        self.payroll.add_payable(invoice)




if __name__ == '__main__':
    company = Company()
    company.fill_data(True)     # Try with True

    print(company.payroll)
    print(company.payroll.amount_to_pay)  # 11840

    
