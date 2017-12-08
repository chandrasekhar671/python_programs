import sys
def convert_dollar(dollar):
    one_dollar = 65
    rupees = dollar*one_dollar
    return rupees
def conversion(rupees):
    t = (rupees*1)/100
    return t
userasks = int(input("enter the dollars to convert it into rupees:"))
amount = convert_dollar(userasks)
final_amount = amount - conversion(amount)
print("you got total amount in rupees is:",final_amount)