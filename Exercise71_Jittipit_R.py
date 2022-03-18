menUlist = []
pricelist = []

def showBill():
    totalPrice = 0
    print("My food".center(20,"-"))
    for number in range(len(menUlist)) :
        print(str(number+1)+".",menUlist[number],pricelist[number],"THB")
        totalPrice += int(pricelist[number])
    print("Total Price :",totalPrice,"THB")
    print("Thank You".center(20,"-"))

while True :
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menUlist.append(menuName)
        pricelist.append(menuPrice)
showBill()
