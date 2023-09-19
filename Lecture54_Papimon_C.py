def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        return False
def showMenu():
    print("-----GP shop-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print(vatCalculate())
    elif userSelected == 2:
        print(priceCalculate())
def vatCalculate():
    totalPrice = int(input("Price : "))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    vat = 7
    total = (price1+price2) + ((price1+price2) * vat / 100)
    return total

print(login())