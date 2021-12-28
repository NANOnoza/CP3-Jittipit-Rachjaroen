def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Try again")
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">> "))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        priceCalculator()
    else:
        print("Please enter a valid number")
        menuSelect()
def vatCalculator():
    totalPrice = int(input("Enter your price : "))
    vat = 7
    result = totalPrice + ((totalPrice * vat) / 100)
    print("ราคารวม vat = "+str(result))
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalprice = price1 + price2
    print("ราคารวมสินค้าคือ "+str(totalprice))
    totalpricevat = ((totalprice*7)/100)+totalprice
    print("ราคารวม vat = "+str(totalpricevat))
login()
print("ขอบคุณที่ใช้บริการ")
