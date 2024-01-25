# Assignment 5 - Exercise 12
# Calculate income tax for the given income by adhering to the rules below

# Request income from user

income = int(input("Enter your income: "))
tax_amount = 0

# Use else-if for formula and conditions

if income <= 10000:
    tax_amount = 0
    
elif income <= 20000:
    income_above_10000 = income - 10000
    tax_amount = income_above_10000 * 10 / 100
    
else:
    # First 10k, no tax
    tax_amount = 0
    
    # Second 10k, 10% tax
    tax_amount = 10000 * 10 / 100  
    
    # Remaining amount, 20% tax
    tax_amount += (income - 20000) * 20 / 100

# Print output

print("Total tax to pay is", tax_amount)