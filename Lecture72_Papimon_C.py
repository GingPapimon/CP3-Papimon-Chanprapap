menuList = []
def showBill():
    totalPrice = 0
    print("------My Food------".center(21))
    for number in range(len(menuList)):
        print(menuList[number], "THB")
        totalPrice += int(menuList[number][1])
    print("Total Price : ", totalPrice, "THB")

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])

showBill()