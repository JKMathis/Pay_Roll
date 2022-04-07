#!/usr/bin/env python3.10

# This is code to take employee info return payroll/tax info

# Step1:Givens: Take the required inputs: Emp_Name, Hours, Rate (rate is hourly)

Emp_Name = input("Please enter your name: ")
Rate = input("Please enter your hourly pay rate: ")
Rate = float(Rate)
Hours = input("Please enter your weekly hours: ")
Hours = float(Hours)

#create payroll dict

Pay_Roll = {'Name':Emp_Name, 'Rate':Rate, 'Hours':Hours}

# calc Gross Pay and add it to Pay_Roll

if Hours <= 40:
     Gross_Pay = float (Hours * Rate)
else:
     Gross_Pay = float((40 * Rate) + ((Hours - 40) * (Rate * 1.5)))

Pay_Roll['Gross Pay'] = Gross_Pay

#calc OT Pay and add it Pay_Roll

if Hours > 40:
    OT_Pay = Gross_Pay - (40 * Rate)
else:
    OT_Pay = 0

Pay_Roll['OT Pay'] = OT_Pay

# calc Fed, State, and FICA + add to dictionary

Fed_Tax = Gross_Pay * 0.1
Pay_Roll['Federal Withholdings'] = Fed_Tax

State_Tax = Gross_Pay * 0.03
Pay_Roll['State Withholding'] = State_Tax

FICA = Gross_Pay * 0.07
Pay_Roll["FICA Withholdings"] = FICA

# calc Net Pay
Total_Tax = Fed_Tax + State_Tax + FICA
Net_Pay = Gross_Pay - Total_Tax
Pay_Roll['Net Pay'] = Net_Pay

# StepOmega:Output: Return: Name, Hours, Rate, Gross Pay, OT Pay(*1.5), Fed Tax(*0.1), State Tax(*0.03), FICA(*0.07), Net Pay
# Print Pay_Roll

Pay_Roll = list(Pay_Roll.values())
print(Pay_Roll)

