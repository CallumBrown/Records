#Callum
#Records class exercise - revision 3



class PaySlipGenerator:
    def __innit__(self):
        self.name = None
        self.number = None
        self.hoursWorked = None
        self.hourlyRate = None
        




new_record = PaySlipGenerator

print("Pay Slip Generator")
print("")
new_record.name = input("Please enter the name of the employee: ")
new_record.number = int(input("Please enter the employee's number: "))
new_record.hoursWorked = int(input("Please enter the hours worked by this employee: "))
new_record.hourlyRate = float(input("Please enter the employee's hourly rate of pay: "))
pay = (new_record.hoursWorked*new_record.hourlyRate)


print("")
print("")
print("*"*35)
print("*Pay Slip                         *")
print("*                                 *")
print("*Name: {0:27}*".format(new_record.name))
print("*Employee Number: {0:<16}*".format(new_record.number))
print("*Hours Worked: {0:<19}*".format(new_record.hoursWorked))
print("*Rate of Pay(in £): {0:<14}*".format(new_record.hourlyRate))
print("*                                 *")
print("*Total Pay: £{0:<21}*".format(pay))
print("*"*35)
