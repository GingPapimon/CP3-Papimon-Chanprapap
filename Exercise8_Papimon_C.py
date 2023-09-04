usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "customer" and passwordInput == "shopping":
    print("---Welcome to Good Shop---")
    print(">> Please select products")
    print("1. cookie:   10 THB")
    print("2. cake:     20 THB")
    print("3. cupcake:  15 THB")
    userSelected = int(input(">>"))
    if userSelected == 1:
        Amount = int(input("Amount : "))
        price = 10 * Amount
        vat = 7
        result = price + (price * vat / 100)
        print("Total  : ", "cookie", Amount, "EA", price, "THB")
        print("------Thank you <3 ------")
    elif userSelected == 2:
        Amount = int(input("Amount : "))
        price = 20 * Amount
        vat = 7
        result = price + (price * vat / 100)
        print("Total  : ", "cake", Amount, "EA", price, "THB")
        print("------Thank you <3 ------")
    elif userSelected == 3:
        Amount = int(input("Amount : "))
        price = 15 * Amount
        vat = 7
        result = price + (price * vat / 100)
        print("Total  : ", "cupcake", Amount, "EA", price, "THB")
        print("------Thank you <3 ------")
    else:
        print("Please try again")
else:
    print("error")