print("Wecome to Petrol Station")
checko=0
ask=int(input("[1]Go get petrol,[2]Go to Cafe:"))
def petrolStation(check):
    def suckasta(check):
        def niggasta():
            petrol=int(input("What type of petrol do you want to get?[1]AI-92 [2]AI-95 [3]Premium [4]Diesel [5]Nah I changed my mind I want to get Cafe:"))
            if petrol==5:
                cafeStation(check)
            elif petrol==1:
                price=1
            elif petrol==2:
                price=2.5
            elif petrol==3:
                price=5
            elif petrol==4:
                price=0.8
            return price,petrol
        price,petrol=niggasta()
        askk=int(input("Do you want to buy with [1]money or [2]liters? [3]Go back and select again:"))
        if askk==3:
            price,petrol=niggasta()
        def askkk(askk,check,price):
            if askk==1:
                mny=int(input(f"How much money do you have?(price per 1 liter is {price}):"))
                check=check+((mny//price)*price)
                print(f"{(mny//price)*price} added to your check!")
                return check
            elif askk==2:
                mny=int(input(f"How much liter you want?(price per 1 liter is {price}):"))
                check=check+(mny*price)
                print(f"{mny*price} added to your check!")
                return check
        mmm=askkk(askk,check,price)
        check=check+mmm
        return check
    ppp=suckasta(check)
    check=check+ppp
    def last(check):
        ask=int(input("Do you want to [1]finish or [2]buy petrol again or go to [3]cafe:"))
        if ask==3:
            cafeStation(check)
        elif ask==1:
            asko=int(input(f"Your total was {check} do you wanna [1]pay or [2]die?"))
            if asko==1:
                print(f"GOODBYE AND THANKS FOR {check}$")
                exit()
            elif asko==2:
                print(3)
                print(3)
                print(1)
                print("KABOOOM, you are not dead you have 5 seconds to runaway!")
                exit()
        elif ask==2:
            check=check+suckasta(check)
            last(check)
    last(check)

def cafeStation(check):
    print("Welcome to Cafe")
    def barista():
        cofe=int(input("What do you wanna buy [1]Cola 2$[2]Water 0.5$ [3]Burger 4$ [4]Pizza 6$ [5]I want to go to the Petrol Station:"))
        if cofe==5:
            petrolStation(check)
        elif cofe==4:
            price=6
        elif cofe==3:
            price=4
        elif cofe==2:
            price=0.5
        elif cofe==1:
            price==2
        return price,cofe
    price,cofe=barista()
    askk=int(input("Do you want to buy with [1]money or [2]quantity? [3]Go back and select again:"))
    if askk==3:
        barista()
    elif askk==2:
        ask=int(input("How much you want?:"))
        check=check+(ask*price)
        print(f"{ask*price} added to your check")
    elif askk==3:
        ask=int(input("How much money you have?:"))
        check=check+(ask//price)
        print(f"{ask//price} quantity you get and {(ask//price)*price} added to your check")
    ask=int(input("Do you want to [1]finish or [2]buy something again or go to [3]petrol station:"))
    if ask==3:
        petrolStation(check)
    elif ask==1:
        asko=int(input(f"Your total was {check} do you wanna [1]pay or [2]die?"))
        if asko==1:
            print(f"GOODBYE AND THANKS FOR {check}$")
            exit()
        elif asko==2:
            print(3)
            print(3)
            print(1)
            print("KABOOOM, you are not dead you have 5 seconds to runaway!")
            exit()
    elif ask==2:
        cafeStation(check)

if ask==1:
    checko=petrolStation(checko)
elif ask==2:
    checko=cafeStation(checko)