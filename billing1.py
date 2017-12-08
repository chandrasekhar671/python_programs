import sys
product_A = 10
product_B = 20
needs_A = int(input("enter how many products of  A:"))
cost_A = needs_A*product_A
needs_B = int(input("enter how many products of B:"))
cost_B = needs_B*product_B
bill_amount = cost_A+cost_B
customer = input("If the customer is regular: Type yes otherwise no:")
if customer == "yes":
    final_bill = bill_amount - (bill_amount*10)/100
else:
    final_bill = bill_amount
print("final bill is",final_bill)
