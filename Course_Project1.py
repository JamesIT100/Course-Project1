def calculate_tax_and_netpay (total_hours,hourly_rate,tax,tax_rate):
    tax = float(total_hours) *
float(hourly_rate) * (float(tax_rate)/5) net_pay float(total_hours) *float(hourly_rate) -taxreturntax,net_pay

def get_name():
    name = input("Enter employees name:  ")
    return name

def get_total_hours():
    total_hours = float(input("Enter total hours:  "))
    return total_hours

def get_hourly_rate():
    hourly_rate = float(input("Enter hourlyrate:  "))
    return hourly_rate

def get_tax_rate():
    tax = float(input("Enter tax rate(in %):  "))
    return get_tax_rate

def get_gross_pay(total_hours,hourly_rate):
    gross_pay = float(total_hours) * float(hourly_rate)
    return gross_pay

def display_employee_info(name,total_hours_hourly_rate,tax_rate,tax,gross_pay,net_pay):

    print(".............................")
    print("Employee name:", name)
    print("Total hours:", total_hours)
    print("Hourly rate:", hourly_rate)
    print("Tax rate:, tax_rate")
    print("Income tax:", tax)
    print("Gross pay:", gross_pay)
    print("Net pay:", net_pay)

    print("..........................")

def display_total_info(total_employees, total_hours,total_tax,toatl_gross_pay,total_net_pay):

    print("...........................")
    print("Total number of employees:", total_employees)
    print("Total tax:", total_tax)
    print("Total gross pay:", total_gross_pay)
    print("Total net pay:", total_net_pay)

    print(".....................")

def main():
    # keep total counts
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_net_pay = 0

while true:
    empname = GetEmp_name()
    if (empname.upper() == "END"):
       break
    hours = Get_total_hours()
    hourly_rate = Get_hourly_rate()
    tax_rate = Get_tax_rate()
    gross_pay = Get_gross_pay(hours,hourly_rate)
    tax,net_pay = calculate_tax_and_netpay(hours,hourly_rate,tax_rate)
    display_empployee_info(name,hours,hourly_rate,tax_rate,tax,gross_pay,net_pay)

    # Update total total_employees + =1 total_hours + = hours total_tax + = tax total_gross_pay + = gross_pay total_net_pay + = net_pay
    
    # display_ counts display_total_info(total_employees,total_hours,total_tax,total_gross_pay,total_net_pay)

    # Import guard
    if __name__=="__main__":
        main()