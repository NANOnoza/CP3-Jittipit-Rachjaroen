price_input = int(input("Enter your price : "))
def vatcalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print("Totalprice : ",vatcalculate(price_input),"THB")
