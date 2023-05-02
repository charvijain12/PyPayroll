# Company Payroll
This project is a Python implementation of a staff payroll system. It models various entities related to payroll management using classes like `StaffMember`, `Employee`, `HourlyEmployee`, `SalariedEmployee`, `CommissionSalariedEmployee`, `Volunteer`, `Item`, `Book`, `Food`, `ValidationRule`, `TaxesValidationRule`, `SuppliersDealsValidationRule`, `InvoiceValidator`, `MandatoryInvoiceValidator`, `CompleteInvoiceValidator`.

Each class has its properties and methods that relate to the entities they model. For example, `Employee` has properties like name, address, day_to_pay and methods like amount_to_pay. `Book` has properties like description, price per unit, quantity, author, etc.

The `InvoiceValidator` and its subclasses are used to validate invoices based on specified validation rules.

This project can be used as a starting point for building a more comprehensive payroll system.


## Getting Started
To get started with this project, follow the below steps:

1. Clone the repository using the command:
```
git clone https://github.com/charvijain12/Company-payroll.git
```

2. Navigate to the cloned repository:
```
cd Company-payroll
```

3. Run the main script:
```
python3 main.py
```

4. The script will run and display the output of the program.


## Contributing
Contributions to this project are welcome. To contribute, follow the standard Github procedure of fork, branch, commit, and pull request.

Please ensure that you follow the project's code style and conventions.


## License
This project is licensed under the MIT License. See the LICENSE file for details.
