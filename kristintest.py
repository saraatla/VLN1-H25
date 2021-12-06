from data.employee_dl import EmployeeDL
from models.employee_model import Employee
from logic.employee_ll import EmployeeLL




# empDL = EmployeeDL()
# emp = Employee('kristin', '123456-3456', 'kristinb20@ru.is','Stigahlíð 84', '564-2728', '824-3732', 'Reykjavik', "L1","keflavik", "yfirmaður")
empDL = EmployeeDL('Svalbard')
listi = ['Jan Jacobsen','123456-0001','jan.jacobsen@nanair.is','Vei 230 12. Longyearbyen','+47 92 09 77 00','+354 777 1337','Svalbard','Lonyearbyen','Manager']
emp = Employee(listi)
edit_employee = empDL.edit_employee('123456-0001',3,'hrauntunga23')


