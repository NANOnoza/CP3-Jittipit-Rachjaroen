print("-------NANO Shop-------")
user = "123"
password = "1234"
user_input = input("Username : ")
password_input = input("password : ")
if user_input == user and password_input == password:
    print("")
    print("Welcome to NANO Shop !")
    print("")
    print("1.Apple 10 THB")
    print("2.Banana 15 THB")
    print("3.Mango 20 THB")
    print("4.Water 10 THB")
    print("5.Milk 15 THB")
    print("6.Sandwich 25 THB")
    print("7.Coke 10 THB")
    print("8.Mama 20 THB")
    print("9.Cake 30 THB")
    print("10.Slurpee 10 THB")
    print("")
    product_input = int(input("ใส่หมายเลขสินค้าที่ต้องการ--> "))
    if product_input == 1:
        product = "Apple"
        cost = 10
    elif product_input == 2:
        product = "Banana"
        cost = 15
    elif product_input == 3:
        product = "Mango"
        cost = 20
    elif product_input == 4:
        product = "Water"
        cost = 10
    elif product_input == 5:
        product = "Milk"
        cost = 15
    elif product_input == 6:
        product = "Sandwich"
        cost = 25
    elif product_input == 7:
        product = "Coke"
        cost = 10
    elif product_input == 8:
        product = "Mama"
        cost = 20
    elif product_input == 9:
        product = "Coke"
        cost = 30
    elif product_input == 10:
        product = "Slurpee"
        cost = 10
    print("")
    print("คุณเลือก",product)
    print("ราคา",cost,"บาท")
    print("")
    itemNumber = int(input("คุณต้องการซื้อทั้งหมดกี่ชิ้น--> "))
    all = itemNumber * cost
    print("")
    print("คุณได้ซื้อ",product,"จำนวน",itemNumber,"ชิ้น")
    print("ราคารวมทั้งหมด",all,"บาท")
    print("")
    print("     ขอบคุณที่ใช้บริการ")
    print("-------NANO Shop-------")
else:
    print("โปรดลองใหม่อีกครั้ง")