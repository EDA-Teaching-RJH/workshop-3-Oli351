cont = "yes"
#cont = input("do you want to continue? ")
while cont:
    cont = input("do you want to continue? ")
    if cont == "no":
        print("quitting application")
        break
    

    else:
        no1 = int(input("number 1: "))
        no2 = int(input("number 2: "))
        opperation = input("opperation: ")

        match opperation:
            case "+":
                result = no1 + no2
                print(f"{no1} + {no2} = {result}")
            case "-":
                result = no1 - no2
                print(f"{no1} - {no2} = {result}")
            case "*":
                result = no1 * no2
                print(f"{no1} * {no2} = {result}")
            case "/":
                if no2 == 0:
                    print("can not divide by 0")
                else:
                    result = no1 / no2
                    print(f"{no1} / {no2} = {result}")
            case "^":
                result = no1 ** no2
                print(f"{no1} ^ {no2} = {result}")
            case "%":
                if no2 == 0:
                    print("can not divide by 0")
                else:
                    result = no1 % no2
                    print(f"{no1} % {no2} = {result}")
            
